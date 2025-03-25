import os
import pytest
import shutil
import tempfile

from src.file_move import move_file

@pytest.fixture
def setup_temp_files():
    """Create a temporary directory and files for testing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create source directory and destination directory
        source_dir = os.path.join(temp_dir, 'source')
        dest_dir = os.path.join(temp_dir, 'destination')
        os.makedirs(source_dir)
        os.makedirs(dest_dir)
        
        # Create a test file
        source_file = os.path.join(source_dir, 'test_file.txt')
        with open(source_file, 'w') as f:
            f.write('Test content')
        
        yield {
            'source_dir': source_dir,
            'dest_dir': dest_dir,
            'source_file': source_file
        }

def test_move_file_to_directory(setup_temp_files):
    """Test moving a file to a different directory."""
    source_file = setup_temp_files['source_file']
    dest_dir = setup_temp_files['dest_dir']
    
    moved_path = move_file(source_file, dest_dir)
    
    assert os.path.exists(moved_path)
    assert os.path.basename(moved_path) == 'test_file.txt'
    assert not os.path.exists(source_file)

def test_move_file_to_specific_path(setup_temp_files):
    """Test moving a file to a specific new path."""
    source_file = setup_temp_files['source_file']
    dest_dir = setup_temp_files['dest_dir']
    new_path = os.path.join(dest_dir, 'renamed_file.txt')
    
    moved_path = move_file(source_file, new_path)
    
    assert os.path.exists(moved_path)
    assert moved_path == new_path
    assert not os.path.exists(source_file)

def test_move_file_error_handling(setup_temp_files):
    """Test various error scenarios."""
    # Non-existent source file
    with pytest.raises(FileNotFoundError):
        move_file('/path/to/nonexistent/file.txt', setup_temp_files['dest_dir'])
    
    # Empty paths
    with pytest.raises(ValueError):
        move_file('', '')
    
    # Try to move a directory
    with pytest.raises(IsADirectoryError):
        move_file(setup_temp_files['source_dir'], setup_temp_files['dest_dir'])

def test_nested_destination_creation(setup_temp_files):
    """Test that nested destination directories are created if they don't exist."""
    source_file = setup_temp_files['source_file']
    dest_dir = setup_temp_files['dest_dir']
    nested_path = os.path.join(dest_dir, 'nested', 'path', 'new_file.txt')
    
    moved_path = move_file(source_file, nested_path)
    
    assert os.path.exists(moved_path)
    assert moved_path == nested_path
    assert not os.path.exists(source_file)