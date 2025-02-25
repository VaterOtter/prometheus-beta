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
    current_sequence = b''
    
    # Compression process
    for byte in input_data:
        # Try to extend current sequence
        test_sequence = current_sequence + bytes([byte])
        
        if test_sequence in dictionary:
            # If sequence exists in dictionary, keep extending
            current_sequence = test_sequence
        else:
            # Output the existing sequence or its reference
            if current_sequence in dictionary:
                output.append(dictionary[current_sequence])
            elif current_sequence:
                # Literal byte output
                output.extend(current_sequence)
            
            # Add new sequence to dictionary
            dictionary[test_sequence] = byte
            current_sequence = bytes([byte])
    
    # Handle remaining sequence
    if current_sequence:
        if current_sequence in dictionary:
            output.append(dictionary[current_sequence])
        else:
            output.extend(current_sequence)
    
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
    
    # Decompression process
    current_sequence = b''
    for byte in compressed_data:
        if byte in dictionary:
            # If byte is in dictionary, retrieve its sequence
            decoded_sequence = dictionary[byte]
            output.extend(decoded_sequence)
            
            if current_sequence:
                # Extend dictionary with new sequence
                dictionary[len(dictionary)] = current_sequence + decoded_sequence[:1]
            
            current_sequence = decoded_sequence
        else:
            # Literal byte or new sequence
            output.append(byte)
            
            if current_sequence:
                # Extend dictionary
                dictionary[len(dictionary)] = current_sequence + bytes([byte])
            
            current_sequence = bytes([byte])
    
    return bytes(output)