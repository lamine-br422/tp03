from datetime import date
from abc import ABC, abstractmethod

class SubscriptionBase(ABC):
    """Abstract base for all subscription types - ISP"""
    
    def __init__(self, student_id: int, amount: float, date_sub, status: str = "unpaid"):
        self.student_id = student_id
        self.amount = amount
        self.date = date_sub
        self.status = status
    
    @abstractmethod
    def display(self) -> str:
        pass
    
    @abstractmethod
    def get_subscription_type(self) -> str:
        pass
    
    def mark_paid(self):
        self.status = "paid"
    
    def mark_unpaid(self):
        self.status = "unpaid"


class Donation(SubscriptionBase):
    """Donation - OCP: new type without modifying base"""
    
    def __init__(self, student_id: int, amount: float, date_sub, donor_name: str = "Anonyme"):
        super().__init__(student_id, amount, date_sub)
        self.donor_name = donor_name
    
    def display(self) -> str:
        return f"🎁 Don de {self.donor_name}: {self.amount}€ le {self.date}"
    
    def get_subscription_type(self) -> str:
        return "Donation"
    
    def to_dict(self) -> dict:
        return {
            'student_id': self.student_id,
            'amount': self.amount,
            'date': str(self.date),
            'status': self.status,
            'type': 'Donation',
            'donor_name': self.donor_name
        }


class MonthlySubscription(SubscriptionBase):
    """Monthly subscription - OCP: new type"""
    
    def display(self) -> str:
        return f"📅 Abonnement mensuel: {self.amount}€/mois le {self.date}"
    
    def get_subscription_type(self) -> str:
        return "Monthly"
    
    def to_dict(self) -> dict:
        return {
            'student_id': self.student_id,
            'amount': self.amount,
            'date': str(self.date),
            'status': self.status,
            'type': 'Monthly'
        }


class AnnualSubscription(SubscriptionBase):
    """Annual subscription with discount - OCP: new type"""
    
    def __init__(self, student_id: int, amount: float, date_sub, discount: float = 0.1):
        super().__init__(student_id, amount, date_sub)
        self.discount = discount
    
    def display(self) -> str:
        final_price = self.amount * (1 - self.discount)
        return f"📊 Abonnement annuel: {self.amount}€ → {final_price}€ (-{self.discount*100}%)"
    
    def get_subscription_type(self) -> str:
        return "Annual"
    
    def to_dict(self) -> dict:
        return {
            'student_id': self.student_id,
            'amount': self.amount,
            'date': str(self.date),
            'status': self.status,
            'type': 'Annual',
            'discount': self.discount
        }


class Subscription(SubscriptionBase):
    """Original Subscription class - SRP: handles only subscription data"""
    
    def __init__(self, student_id: int, amount: float, date_sub: date, status: str = "unpaid"):
        super().__init__(student_id, amount, date_sub, status)
    
    def display(self) -> str:
        return f"Étudiant {self.student_id} | {self.amount}€ | {self.date} | {self.status}"
    
    def get_subscription_type(self) -> str:
        return "Standard"
    
    def to_dict(self) -> dict:
        return {
            'student_id': self.student_id,
            'amount': self.amount,
            'date': str(self.date),
            'status': self.status,
            'type': 'Standard'
        }
    
    @staticmethod
    def from_dict(data: dict):
        """Factory method to create correct subscription type from dict"""
        sub_type = data.get('type', 'Standard')
        
        if sub_type == 'Donation':
            sub = Donation(
                student_id=data['student_id'],
                amount=data['amount'],
                date_sub=date.fromisoformat(data['date']),
                donor_name=data.get('donor_name', 'Anonyme')
            )
        elif sub_type == 'Monthly':
            sub = MonthlySubscription(
                student_id=data['student_id'],
                amount=data['amount'],
                date_sub=date.fromisoformat(data['date'])
            )
        elif sub_type == 'Annual':
            sub = AnnualSubscription(
                student_id=data['student_id'],
                amount=data['amount'],
                date_sub=date.fromisoformat(data['date']),
                discount=data.get('discount', 0.1)
            )
        else:
            sub = Subscription(
                student_id=data['student_id'],
                amount=data['amount'],
                date_sub=date.fromisoformat(data['date']),
                status=data['status']
            )
        
        sub.status = data.get('status', 'unpaid')
        return sub
