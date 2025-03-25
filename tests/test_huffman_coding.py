import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from huffman_coding import (
    huffman_encode, 
    huffman_decode, 
    build_frequency_dict, 
    build_huffman_tree, 
    build_huffman_codes,
    HuffmanNode
)


def test_build_frequency_dict():
    """Test building frequency dictionary."""
    text = "hello world"
    freq_dict = build_frequency_dict(text)
    assert freq_dict == {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
    
    # Test empty input
    assert build_frequency_dict("") == {}


def test_build_huffman_tree():
    """Test building Huffman tree."""
    freq_dict = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
    tree_root = build_huffman_tree(freq_dict)
    
    # Check root node
    assert tree_root is not None
    assert tree_root.char is None
    
    # Test empty input
    assert build_huffman_tree({}) is None


def test_build_huffman_codes():
    """Test generating Huffman codes."""
    # Create a simple Huffman tree
    root = HuffmanNode(None, 100)
    root.left = HuffmanNode('a', 50)
    root.right = HuffmanNode('b', 50)
    
    codes = build_huffman_codes(root)
    assert codes == {'a': '0', 'b': '1'}
    
    # Test empty tree
    assert build_huffman_codes(None) == {}


def test_huffman_encode_decode():
    """Test complete Huffman encoding and decoding."""
    test_cases = [
        "hello world",
        "abracadabra",
        "mississippi river",
        "aaabbbcccdddeeefff"
    ]
    
    for text in test_cases:
        # Encode
        encoded, tree_root = huffman_encode(text)
        
        # Decode
        decoded = huffman_decode(encoded, tree_root)
        
        # Verify
        assert decoded == text


def test_huffman_encode_edge_cases():
    """Test edge cases and error handling for encoding."""
    # Test empty input
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        huffman_encode("")


def test_huffman_decode_edge_cases():
    """Test edge cases and error handling for decoding."""
    # Create a simple Huffman tree
    root = HuffmanNode(None, 100)
    root.left = HuffmanNode('a', 50)
    root.right = HuffmanNode('b', 50)
    
    # Test invalid inputs
    with pytest.raises(ValueError, match="Invalid encoded data or Huffman tree"):
        huffman_decode("", root)
    
    with pytest.raises(ValueError, match="Invalid encoded data or Huffman tree"):
        huffman_decode("10101", None)