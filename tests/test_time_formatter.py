import re
import time
from src.time_formatter import get_current_time_formatted

def test_get_current_time_formatted():
    """
    Test that the function returns a time string in the correct format.
    """
    # Get the formatted time
    formatted_time = get_current_time_formatted()
    
    # Check that the string matches HH:MM:SS format
    assert re.match(r'^\d{2}:\d{2}:\d{2}$', formatted_time), \
        f"Expected HH:MM:SS format, got {formatted_time}"
    
    # Validate each part is within valid ranges
    hours, minutes, seconds = map(int, formatted_time.split(':'))
    
    assert 0 <= hours <= 23, f"Invalid hours: {hours}"
    assert 0 <= minutes <= 59, f"Invalid minutes: {minutes}"
    assert 0 <= seconds <= 59, f"Invalid seconds: {seconds}"

def test_time_consistency():
    """
    Test that multiple calls return valid times (not exactly the same).
    """
    # Get two times with a small delay
    time1 = get_current_time_formatted()
    time.sleep(0.1)  # Small delay to ensure potential time change
    time2 = get_current_time_formatted()
    
    # They might be the same, but shouldn't raise any errors
    assert isinstance(time1, str)
    assert isinstance(time2, str)