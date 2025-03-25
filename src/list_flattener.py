def flatten_nested_list(nested_list):
    """
    Flatten a nested list of arbitrary depth into a single-level list.

    This function recursively flattens a nested list, handling various 
    types of nested structures including lists, tuples, and other iterables.

    Args:
        nested_list (list): A potentially nested list to be flattened.

    Returns:
        list: A flattened list containing all non-iterable elements.

    Raises:
        TypeError: If the input is not iterable.
    """
    # Check if input is None or not iterable
    if nested_list is None:
        return []

    # Initialize the flattened list
    flattened = []

    # Iterate through each item in the nested list
    for item in nested_list:
        # If the item is an iterable (but not a string), recursively flatten
        if hasattr(item, '__iter__') and not isinstance(item, (str, bytes)):
            flattened.extend(flatten_nested_list(item))
        else:
            # If not an iterable, append directly
            flattened.append(item)

    return flattened