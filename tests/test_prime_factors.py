import pytest
from src.prime_factors import get_prime_factors

def test_prime_factors_basic():
    """Test basic prime factorization scenarios."""
    assert get_prime_factors(12) == [2, 2, 3]
    assert get_prime_factors(15) == [3, 5]
    assert get_prime_factors(100) == [2, 2, 5, 5]

def test_prime_factors_prime_numbers():
    """Test prime numbers return themselves."""
    assert get_prime_factors(2) == [2]
    assert get_prime_factors(17) == [17]
    assert get_prime_factors(53) == [53]

def test_prime_factors_edge_cases():
    """Test edge cases like 1 and large numbers."""
    assert get_prime_factors(1) == []
    
    # Large number test
    assert get_prime_factors(84) == [2, 2, 3, 7]

def test_prime_factors_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors(-5)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        get_prime_factors(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        get_prime_factors("12")

def test_prime_factors_sorting():
    """Ensure factors are returned in sorted order."""
    assert get_prime_factors(24) == [2, 2, 2, 3]
    assert get_prime_factors(84) == [2, 2, 3, 7]