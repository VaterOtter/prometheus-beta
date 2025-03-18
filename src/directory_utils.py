import os
from typing import List, Optional

def list_subdirectories(directory_path: str) -> List[str]:
    """
    List all subdirectories in the given directory.

    Args:
        directory_path (str): The path to the directory to search for subdirectories.

    Returns:
        List[str]: A list of subdirectory names (not full paths).

    Raises:
        ValueError: If the provided path is not a directory or does not exist.
    """
    # Validate input
    if not os.path.exists(directory_path):
        raise ValueError(f"Directory path does not exist: {directory_path}")
    
    if not os.path.isdir(directory_path):
        raise ValueError(f"Provided path is not a directory: {directory_path}")
    
    # Get subdirectories
    try:
        # List all entries in the directory and filter for directories
        subdirs = [
            entry.name for entry in os.scandir(directory_path) 
            if entry.is_dir()
        ]
        return subdirs
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing directory: {directory_path}")
    except Exception as e:
        raise RuntimeError(f"Error listing subdirectories: {str(e)}")