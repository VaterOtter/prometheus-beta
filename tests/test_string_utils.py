import pytest
from src.string_utils import rotate_and_reverse

def test_basic_rotation_and_reverse():
    """Test basic string rotation and reversal."""
    assert rotate_and_reverse("hello", 2) == "lohel"

def test_full_rotation():
    """Test rotation equal to string length."""
    assert rotate_and_reverse("python", 6) == "python"

def test_multiple_rotations():
    """Test rotations more than string length."""
    assert rotate_and_reverse("world", 7) == "dlrow"

def test_zero_rotations():
    """Test zero rotations."""
    assert rotate_and_reverse("test", 0) == "test"

def test_empty_string():
    """Test empty string input."""
    assert rotate_and_reverse("", 5) == ""

def test_single_character():
    """Test single character string."""
    assert rotate_and_reverse("a", 3) == "a"

def test_invalid_type_string():
    """Test invalid string type."""
    with pytest.raises(TypeError, match="Input must be a string"):
        rotate_and_reverse(123, 2)

def test_invalid_type_rotations():
    """Test invalid rotations type."""
    with pytest.raises(TypeError, match="Rotations must be an integer"):
        rotate_and_reverse("hello", "2")

def test_negative_rotations():
    """Test negative rotations."""
    with pytest.raises(ValueError, match="Rotations cannot be negative"):
        rotate_and_reverse("hello", -1)