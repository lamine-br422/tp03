from __future__ import annotations
from datetime import date
from abc import ABC, abstractmethod

class Event(ABC):
    """Abstract class for all events - LSP (Liskov Substitution Principle)"""
    
    def __init__(self, event_name: str, description: str, event_date: date):
        self.event_name = event_name
        self.description = description
        self.event_date = event_date
    
    @abstractmethod
    def display(self) -> str:
        """Display event in a nice format"""
        pass
    
    @abstractmethod
    def get_event_type(self) -> str:
        """Get the type of event"""
        pass
    
    @abstractmethod
    def describe(self) -> str:
        """Describe the event in detail"""
        pass
    
    def to_dict(self) -> dict:
        return {
            'event_name': self.event_name,
            'description': self.description,
            'event_date': str(self.event_date),
            'event_type': self.get_event_type()
        }

class Trip(Event):
    """Concrete class: Trip event"""
    
    def __init__(self, event_name: str, description: str, event_date: date, destination: str):
        super().__init__(event_name, description, event_date)
        self.destination = destination
    
    def display(self) -> str:
        return f"🚗 {self.event_name} | {self.destination} | {self.event_date}"
    
    def get_event_type(self) -> str:
        return "Trip"
    
    def describe(self) -> str:
        return f"Voyage éducatif vers {self.destination}. {self.description}"
    
    def to_dict(self) -> dict:
        data = super().to_dict()
        data['destination'] = self.destination
        return data

class Meeting(Event):
    """Concrete class: Meeting event"""
    
    def __init__(self, event_name: str, description: str, event_date: date, room: str = "Salle principale"):
        super().__init__(event_name, description, event_date)
        self.room = room
    
    def display(self) -> str:
        return f"📅 {self.event_name} | {self.room} | {self.event_date}"
    
    def get_event_type(self) -> str:
        return "Meeting"
    
    def describe(self) -> str:
        return f"Réunion dans {self.room}. {self.description}"
    
    def to_dict(self) -> dict:
        data = super().to_dict()
        data['room'] = self.room
        return data

class Competition(Event):
    """Concrete class: Competition event"""
    
    def __init__(self, event_name: str, description: str, event_date: date, prize: str = "Certificat"):
        super().__init__(event_name, description, event_date)
        self.prize = prize
    
    def display(self) -> str:
        return f"🏆 {self.event_name} | Prix: {self.prize} | {self.event_date}"
    
    def get_event_type(self) -> str:
        return "Competition"
    
    def describe(self) -> str:
        return f"Compétition avec prix: {self.prize}. {self.description}"
    
    def to_dict(self) -> dict:
        data = super().to_dict()
        data['prize'] = self.prize
        return data
