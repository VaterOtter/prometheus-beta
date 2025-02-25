"""
Test suite for LZRW compression algorithm implementation.
"""

import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzrw_compression import compress, decompress

def test_empty_input():
    """Test compression and decompression of empty input."""
    empty_data = bytes()
    assert compress(empty_data) == bytes()
    assert decompress(empty_data) == bytes()

def test_simple_compression():
    """Test basic compression and decompression."""
    original_data = b'hello world'
    compressed = compress(original_data)
    decompressed = decompress(compressed)
    assert decompressed == original_data

def test_repeated_data():
    """Test compression of data with repeated sequences."""
    repeated_data = b'aaaaaaaaaabbbbbbbbbb'
    compressed = compress(repeated_data)
    decompressed = decompress(compressed)
    assert decompressed == repeated_data

def test_binary_data():
    """Test compression of binary data."""
    binary_data = bytes([0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5])
    compressed = compress(binary_data)
    decompressed = decompress(compressed)
    assert decompressed == binary_data

def test_large_data():
    """Test compression of larger data set."""
    large_data = b'This is a test of a larger data set with some repetition ' * 10
    compressed = compress(large_data)
    decompressed = decompress(compressed)
    assert decompressed == large_data

def test_type_error():
    """Test that TypeError is raised for non-bytes input."""
    with pytest.raises(TypeError):
        compress("not bytes")
    with pytest.raises(TypeError):
        decompress("not bytes")

def test_reversibility():
    """Ensure that compress and decompress are reversible for various inputs."""
    test_cases = [
        b'hello',
        b'world',
        b'repetitive data data data',
        bytes(range(256)),  # All possible byte values
        b'\x00\x01\x02' * 100
    ]
    
    for data in test_cases:
        compressed = compress(data)
        decompressed = decompress(compressed)
        assert decompressed == data, f"Failed for input: {data}"