"""
Module for logging multiple values in a single statement.

This module provides a flexible logging function that can handle
multiple types of input and log them efficiently.
"""

import logging
from typing import Any, Union, Iterable, Optional


def log_multiple(
    message: str,
    *values: Any,
    log_level: int = logging.INFO,
    separator: str = ' | ',
    extra_values: Optional[list] = None
) -> None:
    """
    Log multiple values in a single statement with flexible formatting.

    Args:
        message (str): The base message to log
        *values (Any): Variable number of values to log
        log_level (int, optional): Logging level. Defaults to logging.INFO
        separator (str, optional): Separator between values. Defaults to ' | '
        extra_values (Optional[list], optional): Additional values to log

    Raises:
        TypeError: If message is not a string
        ValueError: If no logger is configured

    Examples:
        >>> log_multiple("User details:", "John", 25, "New York")
        # Logs: "User details: John | 25 | New York"
    """
    # Validate input
    if not isinstance(message, str):
        raise TypeError("Message must be a string")

    # Combine values from both *values and extra_values parameter
    all_values = list(values)
    if extra_values:
        all_values.extend(extra_values)

    # Prepare values for logging
    value_str = separator.join(str(val) for val in all_values) if all_values else ''
    
    # Combine message and values
    full_message = f"{message} {value_str}".strip()

    # Get the root logger if no logger is configured
    logger = logging.getLogger()

    # Ensure log_level is an integer and within valid range
    if not isinstance(log_level, int):
        log_level = logging.INFO

    # Log the message
    logger.log(log_level, full_message)