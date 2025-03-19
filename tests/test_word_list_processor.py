import os
import pytest
from src.word_list_processor import process_word_list

def test_process_word_list_basic():
    """Test basic functionality of word list processing."""
    # Create a temporary test file
    test_file_path = 'tests/test_word_list.txt'
    with open(test_file_path, 'w') as f:
        f.write("apple\nbanana\ncherry\napple\nBanana\n")
    
    # Process the file
    result = process_word_list(test_file_path)
    
    # Clean up the test file
    os.remove(test_file_path)
    
    # Check the result
    assert result == ['apple', 'banana', 'cherry'], "Should remove duplicates and sort alphabetically"

def test_process_word_list_empty_file():
    """Test processing an empty file."""
    # Create an empty test file
    test_file_path = 'tests/empty_word_list.txt'
    with open(test_file_path, 'w') as f:
        pass
    
    # Process the file
    result = process_word_list(test_file_path)
    
    # Clean up the test file
    os.remove(test_file_path)
    
    # Check the result
    assert result == [], "Should return an empty list for an empty file"

def test_process_word_list_file_not_found():
    """Test handling of non-existent file."""
    with pytest.raises(FileNotFoundError, match="Input file not found"):
        process_word_list('tests/non_existent_file.txt')

def test_process_word_list_whitespace_handling():
    """Test handling of whitespace and case sensitivity."""
    # Create a temporary test file
    test_file_path = 'tests/whitespace_test.txt'
    with open(test_file_path, 'w') as f:
        f.write("  apple  \n banana \n  Apple  \n BANANA\n")
    
    # Process the file
    result = process_word_list(test_file_path)
    
    # Clean up the test file
    os.remove(test_file_path)
    
    # Check the result
    assert result == ['apple', 'banana'], "Should handle whitespace and case insensitivity"