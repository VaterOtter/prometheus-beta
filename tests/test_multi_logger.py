"""
Test suite for multi-value logging function.
"""

import logging
import pytest
import io
import sys
from src.multi_logger import log_multiple


def test_basic_logging(caplog):
    """Test basic logging of multiple values."""
    caplog.set_level(logging.INFO)
    log_multiple("Test:", "value1", 42, 3.14)
    assert "Test: value1 | 42 | 3.14" in caplog.text


def test_no_values(caplog):
    """Test logging with no additional values."""
    caplog.set_level(logging.INFO)
    log_multiple("Test message")
    assert "Test message" in caplog.text


def test_custom_separator(caplog):
    """Test logging with a custom separator."""
    caplog.set_level(logging.INFO)
    log_multiple("Test:", "value1", 42, separator=' - ')
    assert "Test: value1 - 42" in caplog.text


def test_different_log_levels(caplog):
    """Test logging at different log levels."""
    caplog.set_level(logging.DEBUG)
    log_multiple("Debug message", "debug", "info", log_level=logging.DEBUG)
    log_multiple("Warning message", "warning", log_level=logging.WARNING)
    assert "Debug message debug | info" in caplog.text
    assert "Warning message warning" in caplog.text


def test_invalid_message_type():
    """Test raising TypeError for non-string message."""
    with pytest.raises(TypeError, match="Message must be a string"):
        log_multiple(123, "value")


def test_mixed_type_values(caplog):
    """Test logging values of mixed types."""
    caplog.set_level(logging.INFO)
    log_multiple("Mixed types:", 42, "string", [1, 2, 3], {"key": "value"})
    assert "Mixed types: 42 | string | [1, 2, 3] | {'key': 'value'}" in caplog.text


def test_extra_values(caplog):
    """Test logging with extra values list."""
    caplog.set_level(logging.INFO)
    log_multiple("Test:", "value1", extra_values=[42, 3.14])
    assert "Test: value1 | 42 | 3.14" in caplog.text