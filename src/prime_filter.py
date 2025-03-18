def filter_primes(numbers):
    """
    Filter a list of numbers to return only prime numbers.
    
    Args:
        numbers (list): A list of integers to filter.
    
    Returns:
        list: A list of prime numbers from the input list.
    
    Notes:
        - Handles both positive and negative numbers
        - 0 and 1 are not considered prime
        - Negative numbers are considered prime based on their absolute value
    """
    def is_prime(n):
        """
        Check if a number is prime.
        
        Args:
            n (int): Number to check for primality.
        
        Returns:
            bool: True if the number is prime, False otherwise.
        """
        # Convert to absolute value for primality check
        n = abs(n)
        
        # 0 and 1 are not prime
        if n < 2:
            return False
        
        # Check for divisibility up to square root of n
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        
        return True
    
    # Filter and return prime numbers
    return [num for num in numbers if is_prime(num)]