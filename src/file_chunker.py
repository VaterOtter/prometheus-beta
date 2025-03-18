import os
import typing

def split_large_file(
    input_file_path: str, 
    chunk_size_bytes: int, 
    output_dir: typing.Optional[str] = None
) -> typing.List[str]:
    """
    Split a large file into smaller chunks of specified size.

    Args:
        input_file_path (str): Path to the input file to be split
        chunk_size_bytes (int): Size of each chunk in bytes
        output_dir (str, optional): Directory to save chunk files. 
                                    Defaults to same directory as input file.

    Returns:
        List[str]: Paths to the generated chunk files

    Raises:
        ValueError: If chunk size is <= 0 or input file does not exist
        IOError: If there are issues reading/writing files
    """
    # Validate inputs
    if chunk_size_bytes <= 0:
        raise ValueError("Chunk size must be a positive integer")
    
    if not os.path.exists(input_file_path):
        raise ValueError(f"Input file {input_file_path} does not exist")
    
    # Determine output directory
    if output_dir is None:
        output_dir = os.path.dirname(input_file_path) or '.'
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Get base filename for chunks
    base_filename = os.path.basename(input_file_path)
    
    # List to store chunk file paths
    chunk_files = []
    
    try:
        with open(input_file_path, 'rb') as input_file:
            chunk_number = 1
            while True:
                # Read chunk
                chunk = input_file.read(chunk_size_bytes)
                
                # Exit if no more data
                if not chunk:
                    break
                
                # Create chunk filename
                chunk_filename = os.path.join(
                    output_dir, 
                    f"{base_filename}.part{chunk_number:03d}"
                )
                
                # Write chunk
                with open(chunk_filename, 'wb') as chunk_file:
                    chunk_file.write(chunk)
                
                chunk_files.append(chunk_filename)
                chunk_number += 1
    
    except IOError as e:
        raise IOError(f"Error processing file: {e}")
    
    return chunk_files