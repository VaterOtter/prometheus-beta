import logging
from typing import Union

def format_currency_log(amount: Union[int, float], currency: str = '$', locale: str = 'en_US') -> str:
    """
    Format a number with currency symbol and log it.

    Args:
        amount (Union[int, float]): The monetary amount to format and log
        currency (str, optional): Currency symbol. Defaults to '$'.
        locale (str, optional): Locale for formatting. Defaults to 'en_US'.

    Returns:
        str: Formatted currency string

    Raises:
        ValueError: If amount is negative or currency symbol is empty
        TypeError: If amount is not a number
    """
    # Validate inputs
    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be a number")
    
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    
    if not currency or not isinstance(currency, str):
        raise ValueError("Currency symbol must be a non-empty string")

    # Format the number with two decimal places
    formatted_amount = f"{currency}{amount:,.2f}"
    
    # Log the formatted amount
    logging.info(f"Logged amount: {formatted_amount}")
    
    return formatted_amount