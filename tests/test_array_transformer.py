import pytest
from src.array_transformer import transform_array

def test_transform_array_basic():
    """Test basic transformation of non-zero integers"""
    assert transform_array([1, 2, 3]) == [2, 5, 10]

def test_transform_array_with_zero():
    """Test transformation with zero elements"""
    assert transform_array([0, 1, 0, 3]) == [0, 2, 0, 10]

def test_transform_array_empty():
    """Test transformation of an empty list"""
    assert transform_array([]) == []

def test_transform_array_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        transform_array("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        transform_array(123)

def test_transform_array_negative_numbers():
    """Test that ValueError is raised for negative numbers"""
    with pytest.raises(ValueError, match="All input numbers must be non-negative"):
        transform_array([-1, 2, 3])
    with pytest.raises(ValueError, match="All input numbers must be non-negative"):
        transform_array([1, -2, 0])