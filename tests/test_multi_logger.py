"""
Test suite for multi-value logging function.
"""

import logging
import pytest
import io
import sys
from src.multi_logger import log_multiple


def test_basic_logging():
    """Test basic logging of multiple values."""
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Configure a basic logger to stdout
    logging.basicConfig(stream=captured_output, level=logging.INFO, format='%(message)s')

    # Log multiple values
    log_multiple("Test:", "value1", 42, 3.14)

    # Restore stdout
    sys.stdout = sys.__stdout__

    # Check output
    output = captured_output.getvalue().strip()
    assert "Test: value1 | 42 | 3.14" in output


def test_no_values():
    """Test logging with no additional values."""
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Configure a basic logger to stdout
    logging.basicConfig(stream=captured_output, level=logging.INFO, format='%(message)s')

    # Log without additional values
    log_multiple("Test message")

    # Restore stdout
    sys.stdout = sys.__stdout__

    # Check output
    output = captured_output.getvalue().strip()
    assert output == "Test message"


def test_custom_separator():
    """Test logging with a custom separator."""
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Configure a basic logger to stdout
    logging.basicConfig(stream=captured_output, level=logging.INFO, format='%(message)s')

    # Log with custom separator
    log_multiple("Test:", "value1", 42, separator=' - ')

    # Restore stdout
    sys.stdout = sys.__stdout__

    # Check output
    output = captured_output.getvalue().strip()
    assert "Test: value1 - 42" in output


def test_different_log_levels():
    """Test logging at different log levels."""
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Configure a basic logger to stdout
    logging.basicConfig(stream=captured_output, level=logging.DEBUG, format='%(message)s')

    # Log at different levels
    log_multiple("Debug message", logging.DEBUG, "debug", "info")
    log_multiple("Warning message", logging.WARNING, "warning")

    # Restore stdout
    sys.stdout = sys.__stdout__

    # Check output
    output = captured_output.getvalue().strip()
    assert "Debug message debug | info" in output
    assert "Warning message warning" in output


def test_invalid_message_type():
    """Test raising TypeError for non-string message."""
    with pytest.raises(TypeError, match="Message must be a string"):
        log_multiple(123, "value")


def test_mixed_type_values():
    """Test logging values of mixed types."""
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Configure a basic logger to stdout
    logging.basicConfig(stream=captured_output, level=logging.INFO, format='%(message)s')

    # Log mixed types
    log_multiple("Mixed types:", 42, "string", [1, 2, 3], {"key": "value"})

    # Restore stdout
    sys.stdout = sys.__stdout__

    # Check output
    output = captured_output.getvalue().strip()
    assert "Mixed types: 42 | string | [1, 2, 3] | {'key': 'value'}" in output