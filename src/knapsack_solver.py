from typing import List, Tuple, Optional

class Item:
    """
    Represents an item with weight and value for the Knapsack Problem.
    
    Attributes:
        weight (float): The weight of the item.
        value (float): The value of the item.
    """
    def __init__(self, weight: float, value: float):
        """
        Initialize an Item with its weight and value.
        
        Args:
            weight (float): The weight of the item.
            value (float): The value of the item.
        """
        self.weight = weight
        self.value = value

def solve_knapsack(items: List[Item], max_weight: float) -> Tuple[float, List[Item]]:
    """
    Solve the 0/1 Knapsack Problem using dynamic programming.
    
    Args:
        items (List[Item]): List of items to choose from.
        max_weight (float): Maximum weight capacity of the knapsack.
    
    Returns:
        Tuple[float, List[Item]]: A tuple containing the maximum value and the list of selected items.
    
    Raises:
        ValueError: If max_weight is negative or items list is empty.
    """
    # Input validation
    if max_weight < 0:
        raise ValueError("Maximum weight must be non-negative")
    
    if not items:
        return 0.0, []
    
    # Number of items
    n = len(items)
    
    # Create DP table
    # Rows represent items, columns represent weights from 0 to max_weight
    dp = [[0.0 for _ in range(int(max_weight) + 1)] for _ in range(n + 1)]
    
    # Build the dp table
    for i in range(1, n + 1):
        for w in range(int(max_weight) + 1):
            # Current item
            current_item = items[i-1]
            
            # If item can't be included due to weight
            if current_item.weight > w:
                dp[i][w] = dp[i-1][w]
            else:
                # Max of including or excluding the current item
                include_value = dp[i-1][int(w - current_item.weight)] + current_item.value
                exclude_value = dp[i-1][w]
                dp[i][w] = max(exclude_value, include_value)
    
    # Backtrack to find selected items
    selected_items = []
    w = int(max_weight)
    for i in range(n, 0, -1):
        if w >= 0 and dp[i][w] != dp[i-1][w]:
            selected_items.append(items[i-1])
            w -= int(items[i-1].weight)
    
    # Reverse to maintain original order
    selected_items.reverse()
    
    return dp[n][int(max_weight)], selected_items