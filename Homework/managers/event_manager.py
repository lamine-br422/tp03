from datetime import date
from models.event import Trip, Meeting, Competition
from managers.file_storage import FileStorage

class EventManager:
    """SRP: Manages event persistence - DIP uses abstraction"""
    
    def __init__(self, filename: str):
        self.storage = FileStorage(filename)
    
    def save_event(self, event):
        """Save event to storage"""
        self.storage.save(event.to_dict(), 'event_name')
    
    def find_by_name(self, event_name: str):
        """Find event by name"""
        data = self.storage.find_by_field('event_name', event_name)
        if data:
            return self._dict_to_event(data)
        return None
    
    def load_all_events(self) -> list:
        """Load all events"""
        return [self._dict_to_event(data) for data in self.storage.load_all()]
    
    def delete_event(self, event_name: str):
        """Delete event by name"""
        self.storage.delete('event_name', event_name)
    
    @staticmethod
    def _dict_to_event(data: dict):
        """Convert dictionary to appropriate Event subclass"""
        event_type = data.get('event_type')
        
        if event_type == 'Trip':
            return Trip(
                event_name=data['event_name'],
                description=data['description'],
                event_date=date.fromisoformat(data['event_date']),
                destination=data['destination']
            )
        elif event_type == 'Meeting':
            return Meeting(
                event_name=data['event_name'],
                description=data['description'],
                event_date=date.fromisoformat(data['event_date']),
                room=data.get('room', 'Salle principale')
            )
        elif event_type == 'Competition':
            return Competition(
                event_name=data['event_name'],
                description=data['description'],
                event_date=date.fromisoformat(data['event_date']),
                prize=data.get('prize', 'Certificat')
            )
