import pytest
from src.mountain_range import create_mountain_range, Mountain

def test_create_mountain_range_basic():
    """Test basic functionality of creating a mountain range"""
    num_peaks = 5
    mountain_range = create_mountain_range(num_peaks)
    
    # Check correct number of peaks
    assert len(mountain_range) == num_peaks
    
    # Verify each item is a Mountain instance
    assert all(isinstance(mountain, Mountain) for mountain in mountain_range)

def test_create_mountain_range_single_peak():
    """Test creating a mountain range with a single peak"""
    mountain_range = create_mountain_range(1)
    
    assert len(mountain_range) == 1
    assert isinstance(mountain_range[0], Mountain)

def test_create_mountain_range_invalid_input():
    """Test error handling for invalid number of peaks"""
    with pytest.raises(ValueError, match="Number of peaks must be at least 1"):
        create_mountain_range(0)
    
    with pytest.raises(ValueError, match="Number of peaks must be at least 1"):
        create_mountain_range(-1)

def test_mountain_range_attributes():
    """Test the attributes of generated mountains"""
    mountain_range = create_mountain_range(3)
    
    for mountain in mountain_range:
        # Verify name is a string
        assert isinstance(mountain.name, str)
        assert mountain.name
        
        # Verify height is a positive float
        assert isinstance(mountain.height, float)
        assert 100 <= mountain.height <= 8848
        
        # Verify terrain type is a non-empty string
        assert isinstance(mountain.terrain_type, str)
        assert mountain.terrain_type

def test_mountain_range_uniqueness():
    """Ensure generated mountain ranges are not identical"""
    mountain_range1 = create_mountain_range(5)
    mountain_range2 = create_mountain_range(5)
    
    # Checking if all mountains are different (by name or height)
    assert not all(
        m1.name == m2.name and m1.height == m2.height 
        for m1, m2 in zip(mountain_range1, mountain_range2)
    )