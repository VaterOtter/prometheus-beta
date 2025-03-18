import os
import pytest
import zipfile
import tempfile
import shutil

from src.zip_extractor import extract_zip_archive

@pytest.fixture
def sample_zip_file():
    """Create a sample zip file for testing."""
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    
    # Create sample files
    file1_path = os.path.join(temp_dir, 'file1.txt')
    file2_path = os.path.join(temp_dir, 'file2.txt')
    
    with open(file1_path, 'w') as f:
        f.write('Test content 1')
    
    with open(file2_path, 'w') as f:
        f.write('Test content 2')
    
    # Create zip file
    zip_path = os.path.join(temp_dir, 'test_archive.zip')
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(file1_path, arcname='file1.txt')
        zipf.write(file2_path, arcname='file2.txt')
    
    yield zip_path
    
    # Cleanup
    shutil.rmtree(temp_dir)

def test_extract_zip_normal_case(sample_zip_file):
    """Test extracting a zip file to default location."""
    # Get the directory of the zip file
    zip_dir = os.path.dirname(sample_zip_file)
    
    # Extract files
    extracted_files = extract_zip_archive(sample_zip_file)
    
    # Verify extraction
    assert len(extracted_files) == 2
    assert all(os.path.exists(file) for file in extracted_files)
    assert all(os.path.dirname(file) == zip_dir for file in extracted_files)

def test_extract_zip_custom_path(sample_zip_file):
    """Test extracting a zip file to a custom location."""
    # Create a custom extraction directory
    custom_dir = tempfile.mkdtemp()
    
    try:
        # Extract files to custom directory
        extracted_files = extract_zip_archive(sample_zip_file, custom_dir)
        
        # Verify extraction
        assert len(extracted_files) == 2
        assert all(os.path.exists(file) for file in extracted_files)
        assert all(os.path.dirname(file) == custom_dir for file in extracted_files)
    finally:
        # Cleanup
        shutil.rmtree(custom_dir)

def test_extract_nonexistent_file():
    """Test extracting from a non-existent zip file."""
    with pytest.raises(FileNotFoundError):
        extract_zip_archive('/path/to/nonexistent/file.zip')

def test_extract_invalid_zip_file(tmp_path):
    """Test extracting from an invalid zip file."""
    # Create an invalid zip file
    invalid_zip = tmp_path / 'invalid.zip'
    invalid_zip.write_text('Not a real zip file')
    
    with pytest.raises(ValueError):
        extract_zip_archive(str(invalid_zip))

def test_extract_empty_zip(tmp_path):
    """Test extracting an empty zip file."""
    # Create an empty zip file
    empty_zip = tmp_path / 'empty.zip'
    with zipfile.ZipFile(empty_zip, 'w'):
        pass
    
    # Extract empty zip
    extracted_files = extract_zip_archive(str(empty_zip))
    
    # Verify no files extracted
    assert len(extracted_files) == 0