from datetime import datetime, timezone

def timestamp_to_human_readable(timestamp):
    """
    Convert a timestamp to a human-readable date string.

    Args:
        timestamp (int or float): Unix timestamp (seconds since epoch).

    Returns:
        str: Formatted date string in the format 'YYYY-MM-DD HH:MM:SS UTC'.

    Raises:
        TypeError: If timestamp is not a number.
        ValueError: If timestamp is negative or too large.
    """
    # Validate input
    if not isinstance(timestamp, (int, float)):
        raise TypeError("Timestamp must be a number")
    
    # Validate timestamp range
    if timestamp < 0:
        raise ValueError("Timestamp cannot be negative")
    
    try:
        # Convert timestamp to datetime in UTC
        dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
        
        # Format the date in a human-readable way
        return dt.strftime('%Y-%m-%d %H:%M:%S UTC')
    
    except OverflowError:
        raise ValueError("Timestamp is too large to convert")