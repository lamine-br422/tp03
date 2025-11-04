from abc import ABC, abstractmethod
from typing import Any

class Storage(ABC):
    """DIP: Abstraction for different storage mechanisms"""
    
    @abstractmethod
    def save(self, key: str, data: Any) -> bool:
        """Save data with a key"""
        pass
    
    @abstractmethod
    def load(self, key: str) -> Any:
        """Load data by key"""
        pass
    
    @abstractmethod
    def delete(self, key: str) -> bool:
        """Delete data by key"""
        pass
    
    @abstractmethod
    def load_all(self) -> dict:
        """Load all stored data"""
        pass
