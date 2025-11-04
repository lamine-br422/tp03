from __future__ import annotations
from datetime import date
from models.member import Member

class Student(Member):
    """Student class - Inherits from Member, LSP compliant"""
    
    def __init__(self, 
                 full_name: str, 
                 email: str, 
                 phone: str, 
                 address: str, 
                 join_date: date,
                 student_id: int = 0,
                 subscription_status: str = "Pending"):
        super().__init__(full_name, email, phone, address, join_date)
        self.student_id = student_id
        self.subscription_status = subscription_status  # "Pending", "Active", "Inactive"
    
    def display(self) -> str:
        return f"#{self.student_id} {self.full_name} [{self.subscription_status}]"
    
    def check_subscription(self) -> str:
        return self.subscription_status
    
    def update_subscription_status(self, status: str) -> None:
        valid_statuses = ["Pending", "Active", "Inactive"]
        if status in valid_statuses:
            self.subscription_status = status
    
    def to_dict(self) -> dict:
        data = super().to_dict()
        data['student_id'] = self.student_id
        data['subscription_status'] = self.subscription_status
        data['type'] = 'Student'
        return data
    
    @staticmethod
    def from_dict(data: dict) -> Student:
        student = Student(
            full_name=data['full_name'],
            email=data['email'],
            phone=data['phone'],
            address=data['address'],
            join_date=date.fromisoformat(data['join_date']),
            student_id=data.get('student_id', 0),
            subscription_status=data.get('subscription_status', 'Pending')
        )
        student.skills = data.get('skills', [])
        student.interests = data.get('interests', [])
        return student
