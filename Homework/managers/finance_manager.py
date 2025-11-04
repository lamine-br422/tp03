from models.subscription import Subscription
from managers.file_storage import FileStorage

class FinanceManager:
    """SRP: Manages subscription and finance operations - DIP uses abstraction"""
    
    def __init__(self, filename: str):
        self.storage = FileStorage(filename)
    
    def save_subscription(self, subscription: Subscription):
        """Save subscription"""
        self.storage.save(subscription.to_dict(), 'student_id')
    
    def find_by_student_id(self, student_id: int) -> list:
        """Find all subscriptions for a student"""
        data_list = self.storage.find_all_by_field('student_id', student_id)
        return [Subscription.from_dict(data) for data in data_list]
    
    def load_all_subscriptions(self) -> list:
        """Load all subscriptions"""
        return [Subscription.from_dict(data) for data in self.storage.load_all()]
    
    def get_total_revenue(self) -> float:
        """Calculate total revenue from paid subscriptions"""
        subscriptions = self.load_all_subscriptions()
        return sum(sub.amount for sub in subscriptions if sub.status == "paid")
    
    def get_paid_subscriptions(self) -> list:
        """Get all paid subscriptions"""
        subscriptions = self.load_all_subscriptions()
        return [sub for sub in subscriptions if sub.status == "paid"]
    
    def delete_subscription(self, student_id: int):
        """Delete subscription"""
        self.storage.delete('student_id', student_id)
