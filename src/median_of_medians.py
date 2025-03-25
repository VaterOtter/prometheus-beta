def select_kth_smallest(arr, k):
    """
    Implements the median of medians algorithm to find the kth smallest element in an array.
    
    This algorithm guarantees O(n) worst-case time complexity for selection.
    
    Args:
        arr (list): Input list of comparable elements
        k (int): The k-th smallest element to find (1-based indexing)
    
    Returns:
        The kth smallest element in the array
    
    Raises:
        ValueError: If k is out of bounds or input is invalid
    """
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    if k < 1 or k > len(arr):
        raise ValueError(f"k must be between 1 and {len(arr)}, got {k}")
    
    def partition(arr, left, right, pivot_index):
        """
        Partition the array around a pivot element.
        
        Args:
            arr (list): The array to partition
            left (int): Left boundary of the subarray
            right (int): Right boundary of the subarray
            pivot_index (int): Index of the pivot element
        
        Returns:
            int: Final position of the pivot element
        """
        pivot = arr[pivot_index]
        # Move pivot to end
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        
        # Partition around pivot
        store_index = left
        for i in range(left, right):
            if arr[i] < pivot:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        
        # Move pivot to its final place
        arr[right], arr[store_index] = arr[store_index], arr[right]
        
        return store_index
    
    def select(arr, left, right, k):
        """
        Recursive selection of kth smallest element using median of medians.
        
        Args:
            arr (list): The array to search
            left (int): Left boundary of the subarray
            right (int): Right boundary of the subarray
            k (int): The k-th smallest element to find
        
        Returns:
            The kth smallest element
        """
        # If the subarray has less than 5 elements, use simple sorting
        if right - left < 5:
            sorted_subarray = sorted(arr[left:right+1])
            return sorted_subarray[k-1]
        
        # Divide into groups of 5 and find median of medians
        for i in range(left, right+1, 5):
            subright = min(i+4, right)
            median_group = sorted(arr[i:subright+1])
            median = median_group[len(median_group)//2]
            
            # Put medians at the beginning of the array
            median_index = arr.index(median, i, subright+1)
            arr[left + (i-left)//5], arr[median_index] = arr[median_index], arr[left + (i-left)//5]
        
        # Recursively find the median of medians
        num_medians = (right - left) // 5 + 1
        median_of_medians_index = select(arr, left, left + num_medians - 1, num_medians // 2)
        
        # Partition around this median
        pivot_index = arr.index(median_of_medians_index)
        pivot_final_index = partition(arr, left, right, pivot_index)
        
        # Adjust position of k
        pivot_rank = pivot_final_index - left + 1
        
        if k == pivot_rank:
            return arr[pivot_final_index]
        elif k < pivot_rank:
            return select(arr, left, pivot_final_index - 1, k)
        else:
            return select(arr, pivot_final_index + 1, right, k - pivot_rank)
    
    # Create a copy to avoid modifying the original array
    arr_copy = arr.copy()
    return select(arr_copy, 0, len(arr_copy) - 1, k)