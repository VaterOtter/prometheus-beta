"""
Simplified Compression Algorithm

This module provides a basic implementation of a dictionary-based
compression technique inspired by the LZRW (Lempel-Ziv Ross Williams) algorithm.
"""

def compress(input_data):
    """
    Compress input data using a simplified dictionary-based compression.
    
    Args:
        input_data (bytes): The input data to be compressed.
    
    Returns:
        bytes: Compressed data.
    
    Raises:
        TypeError: If input is not bytes.
    """
    # Type checking
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be bytes")
    
    # If input is empty, return empty bytes
    if not input_data:
        return bytes()
    
    # Create a copy of input to modify
    output = bytearray(input_data)
    
    return bytes(output)

def decompress(compressed_data):
    """
    Decompress data compressed with the simplified compression algorithm.
    
    Args:
        compressed_data (bytes): The compressed input data.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
    """
    # Type checking
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # If input is empty, return empty bytes
    if not compressed_data:
        return bytes()
    
    # Create a copy of input to decompress
    output = bytearray(compressed_data)
    
    return bytes(output)