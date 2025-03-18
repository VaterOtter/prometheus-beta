import os
import pytest
import tempfile
import shutil

from src.directory_utils import list_subdirectories

def test_list_subdirectories_normal_case():
    """Test listing subdirectories in a normal scenario."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some subdirectories
        os.makedirs(os.path.join(temp_dir, 'subdir1'))
        os.makedirs(os.path.join(temp_dir, 'subdir2'))
        os.makedirs(os.path.join(temp_dir, 'subdir3'))

        # Get subdirectories
        subdirs = list_subdirectories(temp_dir)

        # Check results
        assert set(subdirs) == {'subdir1', 'subdir2', 'subdir3'}
        assert len(subdirs) == 3

def test_list_subdirectories_empty_directory():
    """Test listing subdirectories in an empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        subdirs = list_subdirectories(temp_dir)
        assert subdirs == []

def test_list_subdirectories_non_existent_path():
    """Test that an error is raised for non-existent paths."""
    with pytest.raises(ValueError, match="Directory path does not exist"):
        list_subdirectories('/path/that/does/not/exist')

def test_list_subdirectories_file_instead_of_directory():
    """Test that an error is raised when a file path is provided."""
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(ValueError, match="Provided path is not a directory"):
            list_subdirectories(temp_file.name)

def test_list_subdirectories_nested_subdirectories():
    """Test that only direct subdirectories are returned."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some nested subdirectories
        os.makedirs(os.path.join(temp_dir, 'subdir1', 'nested1'))
        os.makedirs(os.path.join(temp_dir, 'subdir2'))

        # Get subdirectories
        subdirs = list_subdirectories(temp_dir)

        # Check results
        assert set(subdirs) == {'subdir1', 'subdir2'}
        assert len(subdirs) == 2