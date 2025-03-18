import re
from urllib.parse import urlparse

def is_valid_url(url: str) -> bool:
    """
    Check if the given string is a valid URL.
    
    Args:
        url (str): The URL string to validate
    
    Returns:
        bool: True if the URL is valid, False otherwise
    
    Validates URLs by checking:
    - Proper URL structure
    - Supported schemes
    - Basic format requirements
    """
    # Check if input is a string
    if not isinstance(url, str):
        return False
    
    # Trim whitespace
    url = url.strip()
    
    # Check if URL is empty
    if not url:
        return False
    
    try:
        # Use urlparse to break down the URL
        parsed_url = urlparse(url)
        
        # Check for valid scheme (http, https, ftp, etc.)
        if not parsed_url.scheme:
            return False
        
        # Validate scheme
        valid_schemes = ['http', 'https', 'ftp', 'sftp']
        if parsed_url.scheme not in valid_schemes:
            return False
        
        # Check for a valid network location (domain or IP)
        if not parsed_url.netloc:
            return False
        
        # Split netloc to handle potential port
        domain = parsed_url.netloc.split(':')[0]
        
        # Regex for fully qualified domain names
        domain_regex = re.compile(
            r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z0-9-]{1,63})*\.[A-Za-z]{2,}$'
        )
        
        # Regex for IPv4 addresses
        ip_regex = re.compile(
            r'^(\d{1,3}\.){3}\d{1,3}$'
        )
        
        # Validate domain
        if not (domain_regex.match(domain) or ip_regex.match(domain)):
            return False
        
        return True
    
    except Exception:
        return False