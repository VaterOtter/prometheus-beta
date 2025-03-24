import os
import json
import pytest
from datetime import datetime
from src.session_logger import SessionLogger

def test_session_logger_initialization():
    """Test basic initialization of SessionLogger"""
    logger = SessionLogger()
    assert logger.session_id is not None
    assert 'session_logs' in logger.log_dir
    assert logger.session_state['session_id'] == logger.session_id
    assert 'start_time' in logger.session_state

def test_session_logger_custom_id():
    """Test initialization with custom session ID"""
    custom_id = 'test_session_123'
    logger = SessionLogger(session_id=custom_id)
    assert logger.session_id == custom_id

def test_add_metadata():
    """Test adding metadata to session state"""
    logger = SessionLogger()
    logger.add_metadata('user', 'test_user')
    assert logger.session_state['metadata']['user'] == 'test_user'

def test_add_metadata_empty_key():
    """Test adding metadata with empty key raises ValueError"""
    logger = SessionLogger()
    with pytest.raises(ValueError, match="Metadata key cannot be empty"):
        logger.add_metadata('', 'value')

def test_log_event():
    """Test logging an event"""
    logger = SessionLogger()
    event_details = {'action': 'login', 'status': 'success'}
    logger.log_event('user_login', event_details)
    
    # Check last event
    last_event = logger.session_state['events'][-1]
    assert last_event['type'] == 'user_login'
    assert last_event['details'] == event_details
    assert 'timestamp' in last_event

def test_log_event_empty_type():
    """Test logging an event with empty type raises ValueError"""
    logger = SessionLogger()
    with pytest.raises(ValueError, match="Event type cannot be empty"):
        logger.log_event('', {'action': 'test'})

def test_save_session_log(tmp_path):
    """Test saving session log to file"""
    # Use a temporary directory
    logger = SessionLogger(session_id='test_save', log_dir=str(tmp_path))
    
    # Add some metadata and events
    logger.add_metadata('environment', 'test')
    logger.log_event('test_event', {'data': 'test_data'})
    
    # Save log and verify file
    log_path = logger.save_session_log()
    
    # Verify file exists
    assert os.path.exists(log_path)
    
    # Verify file contents
    with open(log_path, 'r') as log_file:
        saved_state = json.load(log_file)
    
    assert saved_state['session_id'] == 'test_save'
    assert 'start_time' in saved_state
    assert 'end_time' in saved_state
    assert saved_state['metadata']['environment'] == 'test'
    assert len(saved_state['events']) == 1

def test_multiple_events():
    """Test logging multiple events"""
    logger = SessionLogger()
    
    # Log multiple events
    logger.log_event('event1', {'data': 1})
    logger.log_event('event2', {'data': 2})
    
    # Verify events
    assert len(logger.session_state['events']) == 2
    assert logger.session_state['events'][0]['type'] == 'event1'
    assert logger.session_state['events'][1]['type'] == 'event2'