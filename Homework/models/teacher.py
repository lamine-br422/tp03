from __future__ import annotations
from datetime import date
from typing import List
from models.member import Member

class Teacher(Member):
    """Teacher class - Inherits from Member, LSP compliant"""
    
    def __init__(self, 
                 full_name: str, 
                 email: str, 
                 phone: str, 
                 address: str, 
                 join_date: date,
                 teacher_id: int = 0,
                 specialization: str = "General"):
        super().__init__(full_name, email, phone, address, join_date)
        self.teacher_id = teacher_id
        self.specialization = specialization
        self.groups: List[str] = []
        self.assigned_events: List[str] = []
    
    def display(self) -> str:
        return f"Teacher #{self.teacher_id} | {self.full_name} | {self.specialization}"
    
    def display_group(self) -> str:
        groups_str = ", ".join(self.groups) if self.groups else "Aucun groupe"
        return f"Groups of {self.full_name}: {groups_str}"
    
    def assign_event(self, event_name: str) -> None:
        """Assign teacher to an event"""
        if event_name not in self.assigned_events:
            self.assigned_events.append(event_name)
    
    def assign_group(self, group_name: str) -> None:
        """Assign teacher to a group"""
        if group_name not in self.groups:
            self.groups.append(group_name)
    
    def remove_group(self, group_name: str) -> None:
        """Remove teacher from a group"""
        if group_name in self.groups:
            self.groups.remove(group_name)
    
    def get_assigned_events(self) -> List[str]:
        return self.assigned_events.copy()
    
    def to_dict(self) -> dict:
        data = super().to_dict()
        data['teacher_id'] = self.teacher_id
        data['specialization'] = self.specialization
        data['groups'] = self.groups
        data['assigned_events'] = self.assigned_events
        data['type'] = 'Teacher'
        return data
    
    @staticmethod
    def from_dict(data: dict) -> Teacher:
        teacher = Teacher(
            full_name=data['full_name'],
            email=data['email'],
            phone=data['phone'],
            address=data['address'],
            join_date=date.fromisoformat(data['join_date']),
            teacher_id=data.get('teacher_id', 0),
            specialization=data.get('specialization', 'General')
        )
        teacher.skills = data.get('skills', [])
        teacher.interests = data.get('interests', [])
        teacher.groups = data.get('groups', [])
        teacher.assigned_events = data.get('assigned_events', [])
        return teacher
