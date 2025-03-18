import numpy as np

def hungarian_algorithm(cost_matrix):
    """
    Solve the assignment problem using the Hungarian algorithm.
    
    The Hungarian algorithm finds the optimal assignment that minimizes the total cost.
    
    Args:
        cost_matrix (list of lists or numpy.ndarray): A square matrix representing costs 
                                                     for assigning workers to tasks.
    
    Returns:
        list of tuples: Optimal assignment as (worker_index, task_index) pairs.
        float: Total optimal cost of the assignment.
    
    Raises:
        ValueError: If input is not a valid square matrix.
    """
    # Convert input to numpy array for easier manipulation
    try:
        cost_matrix = np.array(cost_matrix, dtype=float)
    except Exception:
        raise ValueError("Input must be a valid matrix of numbers")
    
    # Validate input matrix
    if cost_matrix.ndim != 2 or cost_matrix.shape[0] != cost_matrix.shape[1]:
        raise ValueError("Input must be a square matrix")
    
    n = cost_matrix.shape[0]
    
    # Step 1: Subtract row minimums
    row_min = cost_matrix.min(axis=1)
    cost_matrix = cost_matrix - row_min[:, np.newaxis]
    
    # Step 2: Subtract column minimums
    col_min = cost_matrix.min(axis=0)
    cost_matrix = cost_matrix - col_min
    
    # Step 3: Cover zeros with minimum number of lines
    assignment = []
    covered_rows = set()
    covered_cols = set()
    
    while len(assignment) < n:
        # Find uncovered zeros
        zero_positions = np.argwhere((cost_matrix == 0) & 
                                     ~np.isin(range(n), list(zip(*assignment))[1] if assignment else []) & 
                                     ~np.isin(range(n), [row for row, _ in assignment]))
        
        if len(zero_positions) == 0:
            # If no zeros, add the smallest uncovered value to covered rows and subtract from uncovered columns
            # Find the smallest uncovered value
            mask = np.ones(cost_matrix.shape, dtype=bool)
            mask[list(covered_rows), :] = False
            mask[:, list(covered_cols)] = False
            min_val = cost_matrix[mask].min()
            
            # Subtract from uncovered and add to double-covered
            for row in range(n):
                if row not in covered_rows:
                    cost_matrix[row, :] -= min_val
            for col in range(n):
                if col in covered_cols:
                    cost_matrix[:, col] += min_val
            
            continue
        
        # Select zero and add to assignment
        zero_row, zero_col = zero_positions[0]
        assignment.append((zero_row, zero_col))
    
    # Calculate total cost
    total_cost = sum(cost_matrix[row, col] for row, col in assignment)
    
    return assignment, total_cost