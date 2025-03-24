import os
import pathlib

def find_largest_file(directory):
    """
    Find the largest file in a given directory.

    Args:
        directory (str): Path to the directory to search.

    Returns:
        dict: A dictionary containing file details of the largest file, with keys:
            - 'path': Full path to the largest file
            - 'name': Filename
            - 'size': Size of the file in bytes

    Raises:
        ValueError: If the directory does not exist or is not a directory.
        FileNotFoundError: If no files are found in the directory.
    """
    # Validate input directory
    dir_path = pathlib.Path(directory)
    
    # Check if directory exists and is a directory
    if not dir_path.exists():
        raise ValueError(f"Directory does not exist: {directory}")
    
    if not dir_path.is_dir():
        raise ValueError(f"Provided path is not a directory: {directory}")
    
    # Find all files in the directory (excluding subdirectories)
    files = [f for f in dir_path.iterdir() if f.is_file()]
    
    # Raise error if no files found
    if not files:
        raise FileNotFoundError(f"No files found in directory: {directory}")
    
    # Find the largest file
    largest_file = max(files, key=lambda f: f.stat().st_size)
    
    return {
        'path': str(largest_file),
        'name': largest_file.name,
        'size': largest_file.stat().st_size
    }