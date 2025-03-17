import pytest
from datetime import datetime, timezone
import sys
import os

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from timestamp_converter import timestamp_to_human_readable

def test_valid_timestamp():
    """Test conversion of a standard timestamp."""
    # Using a known timestamp (2023-05-15 10:30:00 UTC)
    timestamp = 1684142400
    assert timestamp_to_human_readable(timestamp) == '2023-05-15 10:30:00 UTC'

def test_zero_timestamp():
    """Test conversion of timestamp zero (epoch start)."""
    timestamp = 0
    assert timestamp_to_human_readable(timestamp) == '1970-01-01 00:00:00 UTC'

def test_float_timestamp():
    """Test conversion of a float timestamp."""
    timestamp = 1684142400.5
    assert timestamp_to_human_readable(timestamp) == '2023-05-15 10:30:00 UTC'

def test_invalid_type_input():
    """Test error handling for non-numeric input."""
    with pytest.raises(TypeError, match="Timestamp must be a number"):
        timestamp_to_human_readable("not a number")
    
    with pytest.raises(TypeError, match="Timestamp must be a number"):
        timestamp_to_human_readable(None)

def test_negative_timestamp():
    """Test error handling for negative timestamp."""
    with pytest.raises(ValueError, match="Timestamp cannot be negative"):
        timestamp_to_human_readable(-100)

def test_extremely_large_timestamp():
    """Test error handling for extremely large timestamp."""
    with pytest.raises(ValueError, match="Timestamp is too large to convert"):
        # An arbitrarily large timestamp that should cause an overflow
        timestamp_to_human_readable(2**64)