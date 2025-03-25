import os

def is_hidden_file(file_path):
    """
    Determine if a file is hidden.

    Args:
        file_path (str): Path to the file to check for hidden status.

    Returns:
        bool: True if the file is hidden, False otherwise.

    Raises:
        TypeError: If file_path is not a string.
        FileNotFoundError: If the file does not exist.
    """
    # Check input type
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    # Normalize the path and check file existence
    normalized_path = os.path.normpath(file_path)
    
    # Check if file exists
    if not os.path.exists(normalized_path):
        raise FileNotFoundError(f"File not found: {normalized_path}")
    
    # Get the filename from the path
    filename = os.path.basename(normalized_path)
    
    # On Unix-like systems (Linux, macOS), hidden files start with a dot
    if filename.startswith('.'):
        return True
    
    # On Windows, use file attributes
    if os.name == 'nt':
        try:
            # Use Windows-specific file attribute check
            import ctypes
            FILE_ATTRIBUTE_HIDDEN = 0x2
            attributes = ctypes.windll.kernel32.GetFileAttributesW(normalized_path)
            return attributes & FILE_ATTRIBUTE_HIDDEN != 0
        except (ImportError, AttributeError):
            # Fallback for systems where ctypes is not available
            pass
    
    return False