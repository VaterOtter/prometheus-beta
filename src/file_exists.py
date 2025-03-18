import os


def check_file_exists(file_path: str) -> bool:
    """
    Check if a file exists at the given path.

    Args:
        file_path (str): The path to the file to check.

    Returns:
        bool: True if the file exists and is a file, False otherwise.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    return os.path.isfile(os.path.abspath(file_path))