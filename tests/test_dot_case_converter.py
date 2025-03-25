import pytest
from src.dot_case_converter import convert_to_dot_case

def test_convert_to_dot_case_basic():
    """Test basic string conversions"""
    assert convert_to_dot_case("HelloWorld") == "hello.world"
    assert convert_to_dot_case("helloWorld") == "hello.world"
    assert convert_to_dot_case("hello_world") == "hello.world"
    assert convert_to_dot_case("hello-world") == "hello.world"

def test_convert_to_dot_case_pascal_case():
    """Test PascalCase conversion"""
    assert convert_to_dot_case("HelloWorldExample") == "hello.world.example"

def test_convert_to_dot_case_snake_case():
    """Test snake_case conversion"""
    assert convert_to_dot_case("hello_world_example") == "hello.world.example"

def test_convert_to_dot_case_kebab_case():
    """Test kebab-case conversion"""
    assert convert_to_dot_case("hello-world-example") == "hello.world.example"

def test_convert_to_dot_case_mixed_case():
    """Test mixed case conversion"""
    assert convert_to_dot_case("Hello_worldExample-test") == "hello.world.example.test"

def test_convert_to_dot_case_empty_string():
    """Test empty string handling"""
    assert convert_to_dot_case("") == ""

def test_convert_to_dot_case_single_word():
    """Test single word conversion"""
    assert convert_to_dot_case("hello") == "hello"

def test_convert_to_dot_case_error_handling():
    """Test error handling for non-string inputs"""
    with pytest.raises(TypeError):
        convert_to_dot_case(123)
    
    with pytest.raises(TypeError):
        convert_to_dot_case(None)