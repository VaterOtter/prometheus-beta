import pytest
import zlib
from src.zlib_compression import compress_data, decompress_data

def test_compress_string():
    """Test compression of a string"""
    original = "Hello, world! This is a test of Zlib compression."
    compressed = compress_data(original)
    assert isinstance(compressed, bytes)

def test_compress_bytes():
    """Test compression of bytes"""
    original = b"Binary data to compress"
    compressed = compress_data(original)
    assert isinstance(compressed, bytes)

def test_decompress_data():
    """Test round-trip compression and decompression"""
    original = "Hello, world! Compression test."
    compressed = compress_data(original)
    decompressed = decompress_data(compressed)
    assert decompressed.decode('utf-8') == original

def test_different_compression_levels():
    """Test different compression levels"""
    data = "Test data for compression levels"
    comp_level_0 = compress_data(data, compression_level=0)
    comp_level_9 = compress_data(data, compression_level=9)
    
    # Both should be valid compressed data
    decompress_data(comp_level_0)
    decompress_data(comp_level_9)

def test_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        compress_data(123)
    
    with pytest.raises(TypeError):
        decompress_data("not bytes")

def test_invalid_compression_level():
    """Test handling of invalid compression levels"""
    with pytest.raises(ValueError):
        compress_data("test", compression_level=-1)
    
    with pytest.raises(ValueError):
        compress_data("test", compression_level=10)

def test_empty_input():
    """Test compression and decompression of empty input"""
    empty_str = ""
    empty_bytes = b""
    
    compressed_str = compress_data(empty_str)
    compressed_bytes = compress_data(empty_bytes)
    
    assert decompress_data(compressed_str) == empty_str.encode('utf-8')
    assert decompress_data(compressed_bytes) == empty_bytes

def test_invalid_compressed_data():
    """Test handling of invalid compressed data"""
    with pytest.raises(zlib.error):
        decompress_data(b'invalid compressed data')