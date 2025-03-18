import pytest
from src.bit_reversal import reverse_bits

def test_reverse_bits_standard_cases():
    """Test standard bit reversal scenarios."""
    # Example from problem description
    assert reverse_bits(43261596) == 964176192
    
    # All 1s
    assert reverse_bits(0xFFFFFFFF) == 0xFFFFFFFF
    
    # All 0s
    assert reverse_bits(0) == 0

def test_reverse_bits_edge_cases():
    """Test edge cases of bit reversal."""
    # Powers of 2
    assert reverse_bits(1) == 2147483648  # 1 -> 10000000000000000000000000000000
    assert reverse_bits(2147483648) == 1  # 10000000000000000000000000000000 -> 1

def test_reverse_bits_invalid_input():
    """Test error handling for invalid inputs."""
    # Negative number
    with pytest.raises(ValueError, match="Input must be a 32-bit unsigned integer"):
        reverse_bits(-1)
    
    # Number too large
    with pytest.raises(ValueError, match="Input must be a 32-bit unsigned integer"):
        reverse_bits(4294967296)
    
    # Non-integer input
    with pytest.raises(ValueError, match="Input must be a 32-bit unsigned integer"):
        reverse_bits("not an integer")

def test_reverse_bits_symmetry():
    """Verify that reversing bits twice returns the original number."""
    test_numbers = [0, 1, 43261596, 0xFFFFFFFF, 2**31]
    
    for num in test_numbers:
        assert reverse_bits(reverse_bits(num)) == num