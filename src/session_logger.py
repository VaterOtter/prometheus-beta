import json
import os
from datetime import datetime
from typing import Dict, Any, Optional

class SessionLogger:
    """
    A class to log the state of an interactive session.
    
    This logger provides methods to track and persist session information,
    including metadata, user details, and custom state data.
    """
    
    def __init__(self, session_id: Optional[str] = None, log_dir: str = 'session_logs'):
        """
        Initialize the SessionLogger.
        
        Args:
            session_id (str, optional): A unique identifier for the session. 
                                        If not provided, a timestamp-based ID is generated.
            log_dir (str, optional): Directory to store session log files. 
                                     Defaults to 'session_logs'.
        """
        # Ensure log directory exists
        os.makedirs(log_dir, exist_ok=True)
        
        # Generate or use provided session ID
        self.session_id = session_id or datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Log directory path
        self.log_dir = log_dir
        
        # Initialize session state
        self.session_state: Dict[str, Any] = {
            'session_id': self.session_id,
            'start_time': datetime.now().isoformat(),
            'metadata': {},
            'events': []
        }
    
    def add_metadata(self, key: str, value: Any) -> None:
        """
        Add metadata to the session state.
        
        Args:
            key (str): Metadata key
            value (Any): Metadata value
        
        Raises:
            ValueError: If key is empty
        """
        if not key:
            raise ValueError("Metadata key cannot be empty")
        
        self.session_state['metadata'][key] = value
    
    def log_event(self, event_type: str, details: Dict[str, Any]) -> None:
        """
        Log an event in the session.
        
        Args:
            event_type (str): Type of event
            details (Dict[str, Any]): Event details
        
        Raises:
            ValueError: If event_type is empty
        """
        if not event_type:
            raise ValueError("Event type cannot be empty")
        
        event = {
            'timestamp': datetime.now().isoformat(),
            'type': event_type,
            'details': details
        }
        self.session_state['events'].append(event)
    
    def save_session_log(self) -> str:
        """
        Save the current session state to a log file.
        
        Returns:
            str: Path to the saved log file
        """
        # Add end time to session state
        self.session_state['end_time'] = datetime.now().isoformat()
        
        # Generate log filename
        log_filename = f"{self.session_id}_session_log.json"
        log_path = os.path.join(self.log_dir, log_filename)
        
        # Write session state to file
        with open(log_path, 'w') as log_file:
            json.dump(self.session_state, log_file, indent=2)
        
        return log_path