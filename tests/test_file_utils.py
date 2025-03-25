import os
import pytest
import tempfile
import pathlib

from src.file_utils import is_hidden_file

def test_unix_hidden_file():
    """Test that files starting with a dot are detected as hidden."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a hidden file
        hidden_file_path = os.path.join(tmpdir, '.hidden_test_file.txt')
        pathlib.Path(hidden_file_path).touch()
        
        assert is_hidden_file(hidden_file_path) == True

def test_non_hidden_file():
    """Test that regular files are not detected as hidden."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a non-hidden file
        visible_file_path = os.path.join(tmpdir, 'visible_test_file.txt')
        pathlib.Path(visible_file_path).touch()
        
        assert is_hidden_file(visible_file_path) == False

def test_non_existent_file():
    """Test that attempting to check a non-existent file raises FileNotFoundError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        non_existent_path = os.path.join(tmpdir, 'does_not_exist.txt')
        
        with pytest.raises(FileNotFoundError):
            is_hidden_file(non_existent_path)

def test_invalid_input_type():
    """Test that passing a non-string input raises TypeError."""
    with pytest.raises(TypeError):
        is_hidden_file(123)
    
    with pytest.raises(TypeError):
        is_hidden_file(None)

def test_file_path_normalization():
    """Test that the function works with different path formats."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a hidden file
        hidden_file_path = os.path.join(tmpdir, '.hidden_test_file.txt')
        pathlib.Path(hidden_file_path).touch()
        
        # Test with absolute path, relative path, and path with '..' and '.'
        abs_path = os.path.abspath(hidden_file_path)
        rel_path = os.path.relpath(hidden_file_path)
        complicated_path = os.path.normpath(os.path.join(tmpdir, '..', os.path.basename(tmpdir), '.hidden_test_file.txt'))
        
        assert is_hidden_file(abs_path) == True
        assert is_hidden_file(rel_path) == True
        assert is_hidden_file(complicated_path) == True