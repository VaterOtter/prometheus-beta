import time
import logging
import pytest
from src.execution_timer import log_execution_time

# Custom logger for testing
class MockLogger:
    def __init__(self):
        self.logs = []
    
    def info(self, message):
        self.logs.append(("info", message))
    
    def error(self, message):
        self.logs.append(("error", message))

def test_log_execution_time():
    # Create a mock logger
    mock_logger = MockLogger()
    
    # Create a test function with the decorator
    @log_execution_time(logger=mock_logger)
    def test_function(x, y):
        time.sleep(0.1)  # Simulate some work
        return x + y
    
    # Call the function
    result = test_function(3, 4)
    
    # Check the result
    assert result == 7
    
    # Check logging
    assert len(mock_logger.logs) == 1
    log_type, log_message = mock_logger.logs[0]
    
    # Verify log type and content
    assert log_type == "info"
    assert "test_function" in log_message
    assert "0.1" in log_message  # Approximate execution time

def test_log_execution_time_with_exception():
    # Create a mock logger
    mock_logger = MockLogger()
    
    # Create a test function that raises an exception
    @log_execution_time(logger=mock_logger)
    def error_function():
        raise ValueError("Test error")
    
    # Verify that the exception is raised
    with pytest.raises(ValueError, match="Test error"):
        error_function()
    
    # Check logging
    assert len(mock_logger.logs) == 1
    log_type, log_message = mock_logger.logs[0]
    
    # Verify error logging
    assert log_type == "error"
    assert "Test error" in log_message

def test_log_execution_time_default_logger():
    # Test with default logger (no custom logger)
    @log_execution_time()
    def simple_function():
        time.sleep(0.05)
        return 42
    
    # Call the function
    result = simple_function()
    
    # Check the result
    assert result == 42