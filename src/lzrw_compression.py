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
    output = bytearray()
    dictionary = {}
    window_start = 0
    
    for i in range(len(input_data)):
        # Check substring from window_start to current index
        current_substring = input_data[window_start:i+1]
        
        if current_substring not in dictionary:
            # When we find a new substring
            # Output the longest match found so far or literal bytes
            if window_start < i:
                match_length = i - window_start
                match_found = False
                for length in range(match_length, 0, -1):
                    substring = input_data[window_start:window_start+length]
                    if substring in dictionary:
                        # Output a reference to the match
                        output.extend([dictionary[substring]])
                        window_start += length
                        match_found = True
                        break
                
                if not match_found:
                    # Output literal bytes if no dictionary match
                    output.extend(input_data[window_start:window_start+1])
                    window_start += 1
            
            # Add the new substring to dictionary
            dictionary[current_substring] = len(dictionary)
    
    # Handle any remaining bytes
    if window_start < len(input_data):
        output.extend(input_data[window_start:])
    
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
    output = bytearray()
    dictionary = {}
    
    i = 0
    while i < len(compressed_data):
        # Check if current byte is a dictionary reference
        if compressed_data[i] < len(dictionary):
            # Retrieve the sequence from dictionary
            sequence = list(dictionary.keys())[compressed_data[i]]
            output.extend(sequence)
            
            # Update dictionary
            if i > 0:
                new_sequence = output[-len(sequence)-1:] if len(output) > 0 else sequence
                dictionary[new_sequence] = len(dictionary)
            
            i += 1
        else:
            # Literal byte
            output.append(compressed_data[i])
            
            # Update dictionary
            if i > 0:
                new_sequence = output[-2:] if len(output) > 1 else bytes([compressed_data[i]])
                dictionary[new_sequence] = len(dictionary)
            
            i += 1
    
    return bytes(output)