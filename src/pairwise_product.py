from typing import List, Union

def calculate_pairwise_products(numbers: List[int]) -> List[int]:
    """
    Calculate the product of all unique pairs of elements in the given list.

    Args:
        numbers (List[int]): A list of integers to calculate pairwise products from.

    Returns:
        List[int]: A list of products for all unique pairs of elements.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
        ValueError: If the input list is empty.

    Examples:
        >>> calculate_pairwise_products([1, 2, 3])
        [2, 3, 6]
        >>> calculate_pairwise_products([-1, 2, 3])
        [-2, -3, 6]
    """
    # Input validation
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if len(numbers) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Validate all elements are integers
    if not all(isinstance(x, int) for x in numbers):
        raise TypeError("All elements must be integers")
    
    # Calculate pairwise products
    products = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            products.append(numbers[i] * numbers[j])
    
    return products