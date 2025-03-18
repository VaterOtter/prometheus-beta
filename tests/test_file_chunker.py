import os
import pytest
import tempfile
import shutil

from src.file_chunker import split_large_file

def test_split_large_file_basic():
    """Test basic file splitting functionality"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a test file
        test_file_path = os.path.join(tmpdir, 'test_file.txt')
        with open(test_file_path, 'wb') as f:
            f.write(b'A' * 1000)  # 1000 bytes
        
        # Split file into 300-byte chunks
        chunks = split_large_file(test_file_path, 300)
        
        assert len(chunks) == 4  # 1000 bytes / 300 bytes = 4 chunks
        
        # Verify chunk contents
        for i, chunk_path in enumerate(chunks, 1):
            with open(chunk_path, 'rb') as chunk:
                content = chunk.read()
                assert len(content) <= 300
                assert len(content) > 0

def test_split_large_file_custom_output_dir():
    """Test splitting file to a custom output directory"""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file_path = os.path.join(tmpdir, 'test_file.txt')
        output_dir = os.path.join(tmpdir, 'chunks')
        
        with open(test_file_path, 'wb') as f:
            f.write(b'B' * 500)
        
        chunks = split_large_file(test_file_path, 200, output_dir)
        
        assert len(chunks) == 3
        for chunk in chunks:
            assert chunk.startswith(output_dir)

def test_split_large_file_invalid_chunk_size():
    """Test error handling for invalid chunk sizes"""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file_path = os.path.join(tmpdir, 'test_file.txt')
        
        with open(test_file_path, 'w') as f:
            f.write('Test')
        
        with pytest.raises(ValueError, match="Chunk size must be a positive integer"):
            split_large_file(test_file_path, 0)
        
        with pytest.raises(ValueError, match="Chunk size must be a positive integer"):
            split_large_file(test_file_path, -100)

def test_split_large_file_nonexistent_file():
    """Test error handling for nonexistent file"""
    with tempfile.TemporaryDirectory() as tmpdir:
        nonexistent_file = os.path.join(tmpdir, 'nonexistent.txt')
        
        with pytest.raises(ValueError, match="Input file.*does not exist"):
            split_large_file(nonexistent_file, 100)

def test_split_single_small_file():
    """Test splitting a file smaller than chunk size"""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file_path = os.path.join(tmpdir, 'small_file.txt')
        
        with open(test_file_path, 'wb') as f:
            f.write(b'Small file content')
        
        chunks = split_large_file(test_file_path, 1000)
        
        assert len(chunks) == 1
        with open(chunks[0], 'rb') as chunk:
            assert chunk.read() == b'Small file content'