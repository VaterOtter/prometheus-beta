def get_prime_factors(n):
    """
    Calculate the prime factors of a positive integer in ascending order.

    Args:
        n (int): A positive integer to factorize.

    Returns:
        list: A sorted list of prime factors.

    Raises:
        ValueError: If the input is less than 1.
        TypeError: If the input is not an integer.
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 1:
        raise ValueError("Input must be a positive integer")
    
    # Handle special cases
    if n == 1:
        return []
    
    # Prime factorization algorithm
    factors = []
    divisor = 2
    
    while divisor * divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    
    # If n is a prime number greater than 1
    if n > 1:
        factors.append(n)
    
    return sorted(factors)