from collections import Counter, defaultdict
import heapq


class HuffmanNode:
    """Represents a node in the Huffman tree."""
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        """Allow comparison for heapq sorting."""
        return self.freq < other.freq


def build_frequency_dict(data):
    """
    Build a frequency dictionary for the input data.
    
    Args:
        data (str): Input string to analyze
    
    Returns:
        dict: Character frequency dictionary
    """
    if not data:
        return {}
    return dict(Counter(data))


def build_huffman_tree(freq_dict):
    """
    Build a Huffman tree from the frequency dictionary.
    
    Args:
        freq_dict (dict): Character frequency dictionary
    
    Returns:
        HuffmanNode: Root of the Huffman tree
    """
    if not freq_dict:
        return None

    # Create heap of nodes
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    # Build tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Create internal node
        internal = HuffmanNode(None, left.freq + right.freq)
        internal.left = left
        internal.right = right

        heapq.heappush(heap, internal)

    return heap[0] if heap else None


def build_huffman_codes(root):
    """
    Generate Huffman codes for each character.
    
    Args:
        root (HuffmanNode): Root of the Huffman tree
    
    Returns:
        dict: Dictionary mapping characters to their Huffman codes
    """
    if not root:
        return {}

    codes = {}

    def traverse(node, current_code=''):
        if not node:
            return

        # Leaf node
        if node.char is not None:
            codes[node.char] = current_code
            return

        # Recursively traverse left and right
        if node.left:
            traverse(node.left, current_code + '0')
        if node.right:
            traverse(node.right, current_code + '1')

    traverse(root)
    return codes


def huffman_encode(data):
    """
    Encode input data using Huffman coding.
    
    Args:
        data (str): Input string to encode
    
    Returns:
        tuple: (encoded string, Huffman tree root)
    
    Raises:
        ValueError: If input is empty
    """
    if not data:
        raise ValueError("Input data cannot be empty")

    # Build frequency dictionary
    freq_dict = build_frequency_dict(data)

    # Build Huffman tree
    tree_root = build_huffman_tree(freq_dict)

    # Generate Huffman codes
    codes = build_huffman_codes(tree_root)

    # Encode the data
    encoded = ''.join(codes[char] for char in data)

    return encoded, tree_root


def huffman_decode(encoded_data, tree_root):
    """
    Decode Huffman encoded data.
    
    Args:
        encoded_data (str): Huffman encoded binary string
        tree_root (HuffmanNode): Root of the Huffman tree
    
    Returns:
        str: Decoded original string
    
    Raises:
        ValueError: If input is invalid
    """
    if not encoded_data or not tree_root:
        raise ValueError("Invalid encoded data or Huffman tree")

    decoded = []
    current = tree_root

    for bit in encoded_data:
        # Traverse down the tree
        current = current.left if bit == '0' else current.right

        # Check if we've reached a leaf node
        if current.char is not None:
            decoded.append(current.char)
            current = tree_root

    return ''.join(decoded)