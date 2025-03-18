import pytest
from src.url_validator import is_valid_url

def test_valid_http_urls():
    assert is_valid_url('http://www.example.com') == True
    assert is_valid_url('https://example.com') == True
    assert is_valid_url('http://subdomain.example.co.uk') == True
    assert is_valid_url('https://example.com:8080') == True

def test_valid_ftp_urls():
    assert is_valid_url('ftp://files.example.com') == True
    assert is_valid_url('sftp://secure.example.com') == True

def test_valid_ip_urls():
    assert is_valid_url('http://192.168.1.1') == True
    assert is_valid_url('https://127.0.0.1') == True

def test_invalid_urls():
    assert is_valid_url('') == False
    assert is_valid_url('   ') == False
    assert is_valid_url('not a url') == False
    assert is_valid_url('htp://example.com') == False  # Incorrect scheme
    assert is_valid_url('http://') == False  # No domain
    assert is_valid_url('http://invalid domain.com') == False  # Invalid domain

def test_edge_cases():
    assert is_valid_url(None) == False
    assert is_valid_url(123) == False
    assert is_valid_url('http://example') == False  # Incomplete domain
    assert is_valid_url('ftp://example.com/path') == True  # Valid with path
    assert is_valid_url('https://example.com?param=value') == True  # Valid with query

def test_unsupported_schemes():
    assert is_valid_url('ssh://example.com') == False
    assert is_valid_url('git://example.com') == False