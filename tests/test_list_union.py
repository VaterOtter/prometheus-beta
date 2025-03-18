import pytest
from src.list_union import find_list_union

def test_basic_union():
    """Test union of two lists with no duplicates."""
    result = find_list_union([1, 2, 3], [4, 5, 6])
    assert result == [1, 2, 3, 4, 5, 6]

def test_union_with_duplicates():
    """Test union of lists with some duplicates."""
    result = find_list_union([1, 2, 3], [3, 4, 5])
    assert result == [1, 2, 3, 4, 5]

def test_union_with_complete_duplicates():
    """Test union of identical lists."""
    result = find_list_union([1, 2, 3], [1, 2, 3])
    assert result == [1, 2, 3]

def test_union_with_empty_lists():
    """Test union when one or both lists are empty."""
    assert find_list_union([], [1, 2, 3]) == [1, 2, 3]
    assert find_list_union([1, 2, 3], []) == [1, 2, 3]
    assert find_list_union([], []) == []

def test_union_preserves_first_occurrence_order():
    """Test that the order of first occurrence is preserved."""
    result = find_list_union([3, 1, 4], [1, 5, 3])
    assert result == [3, 1, 4, 5]

def test_union_with_different_types():
    """Test union with lists containing different types."""
    result = find_list_union([1, 'a', 2], ['a', 3, 'b'])
    assert result == [1, 'a', 2, 3, 'b']

def test_invalid_input_types():
    """Test that TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError):
        find_list_union(123, [1, 2, 3])
    
    with pytest.raises(TypeError):
        find_list_union([1, 2, 3], "not a list")
    
    with pytest.raises(TypeError):
        find_list_union(None, None)