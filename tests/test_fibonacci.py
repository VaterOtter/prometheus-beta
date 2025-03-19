import pytest
from src.fibonacci import fibonacci_sequence

def test_fibonacci_zero():
    """Test generating 0 Fibonacci numbers."""
    assert fibonacci_sequence(0) == []

def test_fibonacci_one():
    """Test generating 1 Fibonacci number."""
    assert fibonacci_sequence(1) == [0]

def test_fibonacci_two():
    """Test generating 2 Fibonacci numbers."""
    assert fibonacci_sequence(2) == [0, 1]

def test_fibonacci_five():
    """Test generating first 5 Fibonacci numbers."""
    assert fibonacci_sequence(5) == [0, 1, 1, 2, 3]

def test_fibonacci_ten():
    """Test generating first 10 Fibonacci numbers."""
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fibonacci_sequence(10) == expected

def test_negative_input():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError, match="n must be a non-negative integer"):
        fibonacci_sequence(-1)

def test_large_input():
    """Test generating a larger sequence to check performance and correctness."""
    result = fibonacci_sequence(20)
    assert len(result) == 20
    
    # Verify Fibonacci property
    for i in range(2, len(result)):
        assert result[i] == result[i-1] + result[i-2]