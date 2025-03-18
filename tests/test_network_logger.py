import pytest
import requests
import logging
from unittest.mock import patch, MagicMock
from src.network_logger import NetworkResponseLogger

class TestNetworkResponseLogger:
    @pytest.fixture
    def logger(self):
        """Create a NetworkResponseLogger instance for testing"""
        return NetworkResponseLogger(log_level=logging.DEBUG)

    def test_successful_get_request(self, logger):
        """Test a successful GET request"""
        with patch('requests.request') as mock_request:
            # Mock a successful response
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.ok = True
            mock_response.headers = {'Content-Type': 'application/json'}
            mock_request.return_value = mock_response

            result = logger.log_request_time('https://example.com')
            
            assert result['status_code'] == 200
            assert result['success'] is True
            assert 'response_time' in result
            assert result['method'] == 'GET'

    def test_request_with_custom_method_and_headers(self, logger):
        """Test request with custom method and headers"""
        with patch('requests.request') as mock_request:
            mock_response = MagicMock()
            mock_response.status_code = 201
            mock_response.ok = True
            mock_request.return_value = mock_response

            result = logger.log_request_time(
                url='https://example.com/create', 
                method='POST', 
                headers={'Authorization': 'Bearer token123'}
            )
            
            assert result['method'] == 'POST'
            mock_request.assert_called_once()

    def test_request_network_error(self, logger):
        """Test handling of network errors"""
        with patch('requests.request') as mock_request:
            mock_request.side_effect = requests.ConnectionError("Network Error")

            with pytest.raises(requests.RequestException):
                logger.log_request_time('https://example.com')

    def test_invalid_url_input(self, logger):
        """Test handling of invalid URL inputs"""
        with pytest.raises(ValueError):
            logger.log_request_time('')

        with pytest.raises(ValueError):
            logger.log_request_time(None)

    def test_timeout_functionality(self, logger):
        """Test request timeout handling"""
        with patch('requests.request') as mock_request:
            mock_request.side_effect = requests.Timeout("Request timed out")

            with pytest.raises(requests.Timeout):
                logger.log_request_time('https://example.com', timeout=0.1)

    def test_response_time_measurement(self, logger):
        """Verify that response time is being measured"""
        with patch('requests.request') as mock_request:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.ok = True
            mock_request.return_value = mock_response

            result = logger.log_request_time('https://example.com')
            
            assert 'response_time' in result
            assert isinstance(result['response_time'], float)
            assert result['response_time'] >= 0