from abc import ABC, abstractmethod
from typing import List

class Registrable(ABC):
    """ISP: Interface for member registration"""
    
    @abstractmethod
    def register_member(self, member_id: int) -> bool:
        """Register a member"""
        pass
    
    @abstractmethod
    def get_registered_members(self) -> List[int]:
        """Get list of registered member IDs"""
        pass
    
    @abstractmethod
    def is_member_registered(self, member_id: int) -> bool:
        """Check if a member is registered"""
        pass
