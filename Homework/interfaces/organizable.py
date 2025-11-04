from abc import ABC, abstractmethod
from datetime import date

class Organizable(ABC):
    """ISP: Interface for scheduling/organizing events"""
    
    @abstractmethod
    def schedule(self, event_date: date) -> None:
        """Schedule the event for a specific date"""
        pass
    
    @abstractmethod
    def get_scheduled_date(self) -> date:
        """Get the scheduled date"""
        pass
    
    @abstractmethod
    def describe(self) -> str:
        """Describe what is being organized"""
        pass
