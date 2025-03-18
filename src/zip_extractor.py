import os
import zipfile

def extract_zip_archive(zip_path, extract_path=None):
    """
    Extract all files from a zip archive to a specified directory.

    Args:
        zip_path (str): Path to the zip file to be extracted.
        extract_path (str, optional): Directory to extract files to. 
                                      If None, extracts to the same directory as the zip file.

    Returns:
        list: List of paths to extracted files.

    Raises:
        FileNotFoundError: If the zip file does not exist.
        ValueError: If the zip_path is not a valid zip file.
        PermissionError: If there are insufficient permissions to extract files.
    """
    # Validate input
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"Zip file not found: {zip_path}")
    
    # Validate it's a zip file
    if not zipfile.is_zipfile(zip_path):
        raise ValueError(f"Not a valid zip file: {zip_path}")
    
    # Determine extraction path
    if extract_path is None:
        extract_path = os.path.dirname(os.path.abspath(zip_path))
    
    # Ensure extraction directory exists
    os.makedirs(extract_path, exist_ok=True)
    
    # List to store extracted file paths
    extracted_files = []
    
    try:
        # Open and extract zip file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Extract all files
            zip_ref.extractall(path=extract_path)
            
            # Get full paths of extracted files
            extracted_files = [
                os.path.join(extract_path, name) 
                for name in zip_ref.namelist()
                if not name.endswith('/')  # Exclude directories
            ]
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to extract files to {extract_path}")
    except Exception as e:
        raise RuntimeError(f"Error extracting zip file: {str(e)}")
    
    return extracted_files