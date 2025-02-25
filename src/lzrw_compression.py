"""
LZRW (Lempel-Ziv Ross Williams) Compression Algorithm Implementation

This module provides functions for LZRW compression and decompression.
LZRW is a simple and fast dictionary-based compression algorithm.
"""

def compress(input_data):
    """
    Compress input data using the LZRW compression algorithm.
    
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
    
    # Initialize compression structures
    output = []
    dictionary = {}
    
    # Sliding window for compression
    window_start = 0
    
    while window_start < len(input_data):
        # Find the longest match in dictionary
        match_length = 0
        match_index = -1
        
        for length in range(min(256, len(input_data) - window_start), 0, -1):
            substring = input_data[window_start:window_start + length]
            
            if substring in dictionary:
                match_length = length
                match_index = dictionary[substring]
                break
        
        if match_length > 0:
            # Found a match in dictionary
            output.append(match_index)
            window_start += match_length
        else:
            # No match, output literal byte
            output.append(input_data[window_start])
            window_start += 1
        
        # Update dictionary
        if window_start > 0:
            new_key = input_data[max(0, window_start-2):window_start]
            dictionary[new_key] = len(dictionary)
    
    return bytes(output)

def decompress(compressed_data):
    """
    Decompress data compressed with the LZRW compression algorithm.
    
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
    
    # Initialize decompression structures
    output = []
    dictionary = {}
    
    for value in compressed_data:
        if value < len(dictionary):
            # Dictionary reference
            sequence = list(dictionary.keys())[value]
            output.extend(sequence)
            
            # Update dictionary
            if output:
                new_key = bytes(output[-2:]) if len(output) > 1 else bytes([value])
                dictionary[new_key] = len(dictionary)
        else:
            # Literal byte
            output.append(value)
            
            # Update dictionary
            if len(output) > 1:
                new_key = bytes(output[-2:])
                dictionary[new_key] = len(dictionary)
    
    return bytes(output)