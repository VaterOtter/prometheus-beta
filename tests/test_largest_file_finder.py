import os
import pytest
import tempfile
import pathlib

from src.largest_file_finder import find_largest_file

def test_find_largest_file_basic():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create multiple files with different sizes
        file1_path = os.path.join(temp_dir, 'small.txt')
        file2_path = os.path.join(temp_dir, 'large.txt')
        
        with open(file1_path, 'w') as f:
            f.write('small')
        
        with open(file2_path, 'w') as f:
            f.write('large' * 100)
        
        # Find largest file
        result = find_largest_file(temp_dir)
        
        assert result['name'] == 'large.txt'
        assert result['size'] == 500
        assert result['path'] == file2_path

def test_find_largest_file_single_file():
    # Create a temporary directory with a single file
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'single.txt')
        
        with open(file_path, 'w') as f:
            f.write('single file content')
        
        # Find largest file
        result = find_largest_file(temp_dir)
        
        assert result['name'] == 'single.txt'
        assert result['size'] == 19
        assert result['path'] == file_path

def test_find_largest_file_empty_directory():
    # Create an empty temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Expect FileNotFoundError for empty directory
        with pytest.raises(FileNotFoundError, match="No files found in directory"):
            find_largest_file(temp_dir)

def test_find_largest_file_nonexistent_directory():
    # Test with a nonexistent directory
    with pytest.raises(ValueError, match="Directory does not exist"):
        find_largest_file('/path/to/nonexistent/directory')

def test_find_largest_file_is_not_directory():
    # Create a temporary file instead of a directory
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(ValueError, match="Provided path is not a directory"):
            find_largest_file(temp_file.name)

def test_find_largest_file_with_zero_byte_files():
    # Create a temporary directory with zero-byte files
    with tempfile.TemporaryDirectory() as temp_dir:
        file1_path = os.path.join(temp_dir, 'empty1.txt')
        file2_path = os.path.join(temp_dir, 'empty2.txt')
        
        # Create zero-byte files
        open(file1_path, 'w').close()
        open(file2_path, 'w').close()
        
        # Should return one of the zero-byte files
        result = find_largest_file(temp_dir)
        
        assert result['size'] == 0
        assert result['name'] in ['empty1.txt', 'empty2.txt']