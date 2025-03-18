import time
import requests
import logging
from typing import Dict, Any, Optional

class NetworkResponseLogger:
    """
    A utility class for logging network request response times and details.
    """
    
    def __init__(self, log_level: int = logging.INFO):
        """
        Initialize the NetworkResponseLogger.
        
        :param log_level: Logging level (default is logging.INFO)
        """
        logging.basicConfig(level=log_level, 
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def log_request_time(self, 
                         url: str, 
                         method: str = 'GET', 
                         headers: Optional[Dict[str, str]] = None, 
                         timeout: float = 10.0) -> Dict[str, Any]:
        """
        Send a network request and log its response time and details.
        
        :param url: The URL to send the request to
        :param method: HTTP method (default is 'GET')
        :param headers: Optional headers for the request
        :param timeout: Request timeout in seconds (default is 10)
        :return: Dictionary containing request details and response metrics
        """
        # Validate inputs
        if not url or not isinstance(url, str):
            raise ValueError("URL must be a non-empty string")
        
        # Prepare request details
        headers = headers or {}
        start_time = time.time()
        
        try:
            # Send the request
            response = requests.request(
                method=method.upper(), 
                url=url, 
                headers=headers, 
                timeout=timeout
            )
            
            # Calculate response time
            end_time = time.time()
            response_time = end_time - start_time
            
            # Log request details
            log_message = (
                f"Network Request: {method} {url} | "
                f"Status: {response.status_code} | "
                f"Response Time: {response_time:.4f} seconds"
            )
            self.logger.info(log_message)
            
            # Return comprehensive metrics
            return {
                'url': url,
                'method': method,
                'status_code': response.status_code,
                'response_time': response_time,
                'headers': dict(response.headers),
                'success': response.ok
            }
        
        except requests.RequestException as e:
            # Handle network-related errors
            end_time = time.time()
            response_time = end_time - start_time
            
            error_message = (
                f"Network Request Failed: {method} {url} | "
                f"Error: {str(e)} | "
                f"Time Elapsed: {response_time:.4f} seconds"
            )
            self.logger.error(error_message)
            
            raise