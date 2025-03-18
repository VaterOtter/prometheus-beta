def find_list_union(list1, list2):
    """
    Find the union of two lists, removing duplicates and preserving order.

    Args:
        list1 (list): The first input list.
        list2 (list): The second input list.

    Returns:
        list: A list containing unique elements from both input lists,
              maintaining the order of first occurrence.

    Raises:
        TypeError: If input arguments are not lists.
    """
    # Validate input types
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both arguments must be lists")
    
    # Use a dictionary to maintain order and remove duplicates
    union_dict = {}
    
    # Add elements from list1, preserving their original order
    for item in list1:
        union_dict[item] = None
    
    # Add elements from list2, preserving their order after list1
    for item in list2:
        union_dict[item] = None
    
    # Return the keys (unique elements) as a list
    return list(union_dict.keys())