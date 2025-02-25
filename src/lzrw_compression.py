"""
LZRW (Lempel-Ziv Ross Williams) Compression Algorithm Implementation

This module provides functions for LZRW compression and decompression.
LZRW is a simple and fast dictionary-based compression algorithm.
"""

def compress(input_data):
    """
    Compress input data using a simple LZRW-inspired compression algorithm.
    
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
    output = bytearray()
    dictionary = {}
    
    # Sliding window
    window_start = 0
    
    while window_start < len(input_data):
        # Initialize variables for best match
        best_match_length = 0
        best_match_index = -1
        
        # Try to find the longest match in the dictionary
        for length in range(min(256, len(input_data) - window_start), 0, -1):
            current_substring = input_data[window_start:window_start + length]
            
            if current_substring in dictionary:
                best_match_length = length
                best_match_index = dictionary[current_substring]
                break
        
        if best_match_length > 0:
            # Found a match
            output.append(best_match_index)
            window_start += best_match_length
        else:
            # No match, output literal byte
            output.append(input_data[window_start])
            window_start += 1
        
        # Update dictionary with sliding window
        if window_start > 0:
            # Use small, overlapping sequences as dictionary keys
            context = input_data[max(0, window_start-2):window_start]
            if len(context) >= 1:
                dictionary[context] = len(dictionary) % 256
    
    return bytes(output)

def decompress(compressed_data):
    """
    Decompress data compressed with the custom LZRW algorithm.
    
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
    output = bytearray()
    dictionary = {}
    
    for current_byte in compressed_data:
        if current_byte < len(dictionary):
            # Retrieve sequence from dictionary
            sequence = list(dictionary.keys())[current_byte]
            output.extend(sequence)
        else:
            # Literal byte
            output.append(current_byte)
        
        # Update dictionary
        if len(output) > 1:
            # Use last 1-2 bytes as context
            context = bytes(output[-2:]) if len(output) > 1 else bytes([current_byte])
            dictionary[context] = len(dictionary) % 256
    
    return bytes(output)