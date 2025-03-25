import os
import pytest
import tempfile

from src.remove_empty_lines import remove_empty_lines

def test_remove_empty_lines_normal_case():
    # Create a temporary input file with some empty lines
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_input:
        temp_input.write("Hello\n\nWorld\n\n\nPython\n")
        temp_input_path = temp_input.name

    # Create a temporary output file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_output:
        temp_output_path = temp_output.name

    # Remove empty lines
    removed_count = remove_empty_lines(temp_input_path, temp_output_path)

    # Check the result
    assert removed_count == 3
    with open(temp_output_path, 'r') as f:
        content = f.read()
    
    assert content == "Hello\nWorld\nPython\n"

    # Clean up temporary files
    os.unlink(temp_input_path)
    os.unlink(temp_output_path)

def test_remove_empty_lines_overwrite():
    # Create a temporary input file with some empty lines
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello\n\nWorld\n\n\nPython\n")
        temp_file_path = temp_file.name

    # Remove empty lines (overwriting the original file)
    removed_count = remove_empty_lines(temp_file_path)

    # Check the result
    assert removed_count == 3
    with open(temp_file_path, 'r') as f:
        content = f.read()
    
    assert content == "Hello\nWorld\nPython\n"

    # Clean up temporary file
    os.unlink(temp_file_path)

def test_remove_empty_lines_whitespace_only():
    # Create a temporary input file with whitespace-only lines
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello\n   \n\t\nWorld\n")
        temp_file_path = temp_file.name

    # Remove empty lines
    removed_count = remove_empty_lines(temp_file_path)

    # Check the result
    assert removed_count == 2
    with open(temp_file_path, 'r') as f:
        content = f.read()
    
    assert content == "Hello\nWorld\n"

    # Clean up temporary file
    os.unlink(temp_file_path)

def test_remove_empty_lines_no_empty_lines():
    # Create a temporary input file with no empty lines
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello\nWorld\nPython\n")
        temp_file_path = temp_file.name

    # Remove empty lines
    removed_count = remove_empty_lines(temp_file_path)

    # Check the result
    assert removed_count == 0
    with open(temp_file_path, 'r') as f:
        content = f.read()
    
    assert content == "Hello\nWorld\nPython\n"

    # Clean up temporary file
    os.unlink(temp_file_path)

def test_remove_empty_lines_file_not_found():
    # Test FileNotFoundError is raised for non-existent file
    with pytest.raises(FileNotFoundError):
        remove_empty_lines("/path/to/non/existent/file.txt")

def test_remove_empty_lines_invalid_input_type():
    # Test TypeError is raised for non-string inputs
    with pytest.raises(TypeError):
        remove_empty_lines(123)
    
    with pytest.raises(TypeError):
        remove_empty_lines("input.txt", 456)