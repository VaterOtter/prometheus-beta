from typing import List, Optional, Any

class TreeNode:
    """
    Represents a node in a binary tree.
    
    Attributes:
        val (Any): The value stored in the node
        left (Optional[TreeNode]): Left child node
        right (Optional[TreeNode]): Right child node
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzag_level_order_traversal(root: Optional[TreeNode]) -> List[List[Any]]:
    """
    Perform a zigzag (spiral) level order traversal of a binary tree.
    
    In a zigzag traversal, nodes are visited level by level, 
    alternating between left-to-right and right-to-left directions.
    
    Args:
        root (Optional[TreeNode]): The root node of the binary tree
    
    Returns:
        List[List[Any]]: A list of levels, where each level is a list of node values
        
    Examples:
        # Example tree:
        #     3
        #    / \
        #   9  20
        #      / \
        #     15  7
        # Would return: [[3], [20,9], [15,7]]
    
    Time Complexity: O(n), where n is the number of nodes in the tree
    Space Complexity: O(n)
    """
    # Handle empty tree case
    if not root:
        return []
    
    # Initialize result and queue for level-order traversal
    result = []
    queue = [root]
    left_to_right = True
    
    while queue:
        # Number of nodes at current level
        level_size = len(queue)
        current_level = []
        
        # Process all nodes at current level
        for _ in range(level_size):
            # Remove the first node from the queue
            node = queue.pop(0)
            
            # Add node value to current level
            current_level.append(node.val)
            
            # Add child nodes to queue for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Reverse the level if needed for zigzag pattern
        if not left_to_right:
            current_level.reverse()
        
        # Add current level to result
        result.append(current_level)
        
        # Flip direction for next level
        left_to_right = not left_to_right
    
    return result