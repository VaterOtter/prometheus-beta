import pytest
from src.text_replacer import replace_words

def test_basic_replacement():
    """Test basic word replacement"""
    text = "hello world"
    replacements = {"hello": "hi", "world": "earth"}
    assert replace_words(text, replacements) == "hi earth"

def test_multiple_replacements():
    """Test multiple replacements in a single text"""
    text = "the quick brown fox jumps over the lazy dog"
    replacements = {"quick": "slow", "brown": "red", "lazy": "active"}
    assert replace_words(text, replacements) == "the slow red fox jumps over the active dog"

def test_no_replacements():
    """Test when no replacements match"""
    text = "hello world"
    replacements = {"python": "java"}
    assert replace_words(text, replacements) == "hello world"

def test_case_sensitive_replacement():
    """Test that replacements are case-sensitive"""
    text = "Hello World hello world"
    replacements = {"hello": "hi"}
    assert replace_words(text, replacements) == "Hello World hi world"

def test_empty_text():
    """Test with empty text"""
    text = ""
    replacements = {"hello": "hi"}
    assert replace_words(text, replacements) == ""

def test_invalid_text_type():
    """Test raising TypeError for non-string text"""
    with pytest.raises(TypeError, match="Input text must be a string"):
        replace_words(123, {"hello": "hi"})

def test_invalid_replacements_type():
    """Test raising TypeError for non-dictionary replacements"""
    with pytest.raises(TypeError, match="Replacements must be a dictionary"):
        replace_words("hello", "not a dict")

def test_invalid_replacement_key():
    """Test raising ValueError for invalid replacement key"""
    with pytest.raises(ValueError, match="Replacement keys must be non-empty strings"):
        replace_words("hello", {123: "hi"})

def test_invalid_replacement_value():
    """Test raising ValueError for invalid replacement value"""
    with pytest.raises(ValueError, match="Replacement values must be strings"):
        replace_words("hello", {"hello": 123})

def test_empty_key_replacement():
    """Test raising ValueError for empty string key"""
    with pytest.raises(ValueError, match="Replacement keys must be non-empty strings"):
        replace_words("hello", {"": "hi"})