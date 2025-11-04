from abc import ABC, abstractmethod
from datetime import date

class Payable(ABC):
    """ISP: Interface for payment operations - segregated responsibility"""
    
    @abstractmethod
    def process_payment(self) -> bool:
        """Process payment and return success status"""
        pass
    
    @abstractmethod
    def get_amount(self) -> float:
        """Get payment amount"""
        pass
    
    @abstractmethod
    def get_status(self) -> str:
        """Get payment status"""
        pass
