import pytest
import logging
from src.currency_formatter import format_currency_log

def test_default_currency_formatting():
    """Test default currency formatting with USD."""
    result = format_currency_log(1234.56)
    assert result == '$1,234.56'

def test_custom_currency_symbol():
    """Test custom currency symbol."""
    result = format_currency_log(1234.56, currency='€')
    assert result == '€1,234.56'

def test_integer_input():
    """Test formatting with integer input."""
    result = format_currency_log(1234)
    assert result == '$1,234.00'

def test_float_precision():
    """Test float precision rounding."""
    result = format_currency_log(1234.567)
    assert result == '$1,234.57'

def test_negative_amount_raises_error():
    """Test that negative amounts raise a ValueError."""
    with pytest.raises(ValueError, match="Amount cannot be negative"):
        format_currency_log(-100)

def test_invalid_currency_symbol():
    """Test that empty currency symbol raises an error."""
    with pytest.raises(ValueError, match="Currency symbol must be a non-empty string"):
        format_currency_log(100, currency='')

def test_invalid_amount_type():
    """Test that non-numeric amounts raise a TypeError."""
    with pytest.raises(TypeError, match="Amount must be a number"):
        format_currency_log('not a number')

def test_logging(caplog):
    """Test that the function logs the formatted amount."""
    caplog.set_level(logging.INFO)
    format_currency_log(1234.56)
    assert "Logged amount: $1,234.56" in caplog.text