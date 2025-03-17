def find_gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm.
    
    Args:
        a (int): First integer number
        b (int): Second integer number
    
    Returns:
        int: The greatest common divisor of a and b
    
    Raises:
        TypeError: If inputs are not integers
        ValueError: If either input is negative
    """
    # Type checking
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    
    # Non-negative checking
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    # Edge case: if either number is 0, return the other number
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Euclidean algorithm
    while b:
        a, b = b, a % b
    
    return a