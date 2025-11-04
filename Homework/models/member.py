from datetime import date
from typing import List

class Member:
    """Member class - SRP: handles only member data"""
    
    def __init__(self, full_name: str, email: str, phone: str, address: str, join_date: date):
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.address = address
        self.join_date = join_date
        self.skills: List[str] = []
        self.interests: List[str] = []
    
    def add_skill(self, skill: str):
        if skill not in self.skills:
            self.skills.append(skill)
    
    def add_interest(self, interest: str):
        if interest not in self.interests:
            self.interests.append(interest)
    
    def display(self) -> str:
        return f"{self.full_name} | {self.email} | {self.phone} | {self.address} | {self.join_date}"
    
    def to_dict(self) -> dict:
        return {
            'full_name': self.full_name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'join_date': str(self.join_date),
            'skills': self.skills,
            'interests': self.interests
        }
    
    @staticmethod
    def from_dict(data: dict) -> 'Member':
        member = Member(
            full_name=data['full_name'],
            email=data['email'],
            phone=data['phone'],
            address=data['address'],
            join_date=date.fromisoformat(data['join_date'])
        )
        member.skills = data.get('skills', [])
        member.interests = data.get('interests', [])
        return member
