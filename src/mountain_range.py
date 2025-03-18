import random
from typing import List, Dict, Union

class Mountain:
    """
    Represents a mountain with key characteristics.
    
    Attributes:
        name (str): Name of the mountain
        height (float): Height of the mountain in meters
        terrain_type (str): Type of terrain surrounding the mountain
    """
    def __init__(self, name: str, height: float, terrain_type: str):
        """
        Initialize a Mountain object.
        
        Args:
            name (str): Name of the mountain
            height (float): Height in meters
            terrain_type (str): Surrounding terrain type
        """
        self.name = name
        self.height = height
        self.terrain_type = terrain_type

def create_mountain_range(num_peaks: int) -> List[Mountain]:
    """
    Generate a list of mountain range objects.
    
    Args:
        num_peaks (int): Number of mountain peaks to generate
    
    Returns:
        List[Mountain]: A list of Mountain objects
    
    Raises:
        ValueError: If num_peaks is less than 1
    """
    # Validate input
    if num_peaks < 1:
        raise ValueError("Number of peaks must be at least 1")
    
    # Predefined terrain types and name prefixes
    terrain_types = ['alpine', 'volcanic', 'sedimentary', 'glacial', 'rocky']
    name_prefixes = ['Mount', 'Peak', 'Summit', 'Ridge']
    
    # Generate mountains
    mountains = []
    for i in range(num_peaks):
        name = f"{random.choice(name_prefixes)} {i+1}"
        height = round(random.uniform(100, 8848), 2)  # Ranges from 100m to Mt. Everest height
        terrain_type = random.choice(terrain_types)
        
        mountains.append(Mountain(name, height, terrain_type))
    
    return mountains