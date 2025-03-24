import pytest
import logging
import src.memory_logger as memory_logger
import psutil

class MockLogger:
    def __init__(self):
        self.info_logs = []
        self.error_logs = []
    
    def info(self, message):
        self.info_logs.append(message)
    
    def error(self, message):
        self.error_logs.append(message)

def test_log_memory_usage_returns_dict():
    """Test that the function returns a dictionary with correct keys."""
    stats = memory_logger.log_memory_usage()
    
    assert isinstance(stats, dict)
    assert set(stats.keys()) == {'total', 'available', 'used', 'percent'}

def test_log_memory_usage_with_custom_logger():
    """Test logging with a custom logger."""
    mock_logger = MockLogger()
    stats = memory_logger.log_memory_usage(mock_logger)
    
    assert len(mock_logger.info_logs) > 0
    assert 'Memory Usage Statistics' in mock_logger.info_logs[0]

def test_memory_stats_accuracy():
    """Test that memory statistics are within expected ranges."""
    stats = memory_logger.log_memory_usage()
    
    # Total memory should be positive
    assert stats['total'] > 0
    
    # Percent should be between 0 and 100
    assert 0 <= stats['percent'] <= 100
    
    # Available and used memory should be less than or equal to total
    assert stats['available'] <= stats['total']
    assert stats['used'] <= stats['total']

def test_memory_stats_match_psutil():
    """Verify that function stats match psutil's memory stats."""
    stats = memory_logger.log_memory_usage()
    psutil_memory = psutil.virtual_memory()
    
    # Check that our calculations are close to psutil's
    assert abs(stats['total'] - psutil_memory.total / (1024 * 1024)) < 1
    assert abs(stats['percent'] - psutil_memory.percent) < 1