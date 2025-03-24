"""
Module for logging multiple values in a single statement.

This module provides a flexible logging function that can handle
multiple types of input and log them efficiently.
"""

import logging
from typing import Any, Union, Iterable


def log_multiple(
    message: str,
    log_level: int = logging.INFO,
    *values: Any,
    separator: str = ' | '
) -> None:
    """
    Log multiple values in a single statement with flexible formatting.

    Args:
        message (str): The base message to log
        log_level (int, optional): Logging level. Defaults to logging.INFO
        *values (Any): Variable number of values to log
        separator (str, optional): Separator between values. Defaults to ' | '

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

    # Prepare values for logging
    try:
        # Convert all values to strings and join them
        value_str = separator.join(str(val) for val in values) if values else ''
        
        # Combine message and values
        full_message = f"{message} {value_str}".strip()

        # Get the root logger if no logger is configured
        logger = logging.getLogger()

        # If no handlers are configured, add a default console handler
        if not logger.handlers:
            console_handler = logging.StreamHandler()
            formatter = logging.Formatter('%(message)s')
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)
            logger.setLevel(logging.INFO)

        # Log the message at the specified level
        logger.log(log_level, full_message)

    except Exception as e:
        # Catch and re-raise any unexpected errors
        raise ValueError(f"Failed to log message: {str(e)}") from e