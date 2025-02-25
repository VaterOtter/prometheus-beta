"""
Simplified LZRW-inspired Compression Algorithm

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
    
    # Initialization
    output = bytearray()
    dictionary = {}
    current_sequence = bytearray()
    
    for byte in input_data:
        # Extend current sequence
        current_sequence.append(byte)
        
        # Check if current sequence exists in dictionary
        if bytes(current_sequence) not in dictionary:
            # New sequence found
            if len(current_sequence) > 1:
                # Try to find the longest existing prefix
                prefix = current_sequence[:-1]
                if prefix in dictionary:
                    # Output dictionary reference or literal
                    output.append(dictionary[prefix])
                else:
                    # Output individual bytes
                    output.extend(prefix)
            
            # Add new sequence to dictionary
            dictionary[bytes(current_sequence)] = len(dictionary)
            
            # Reset current sequence to last byte
            current_sequence = bytearray([byte])
    
    # Handle remaining sequence
    if current_sequence:
        if bytes(current_sequence) in dictionary:
            output.append(dictionary[bytes(current_sequence)])
        else:
            output.extend(current_sequence)
    
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
    
    # Initialization
    output = bytearray()
    dictionary = {}
    
    for value in compressed_data:
        if value < len(dictionary):
            # Dictionary reference
            sequence = list(dictionary.keys())[value]
            output.extend(sequence)
            
            # Update dictionary if possible
            if output:
                new_entry = bytes(output[-2:]) if len(output) > 1 else bytes([value])
                dictionary[new_entry] = len(dictionary)
        else:
            # Literal byte
            output.append(value)
            
            # Update dictionary
            if len(output) > 1:
                new_entry = bytes(output[-2:])
                dictionary[new_entry] = len(dictionary)
    
    return bytes(output)