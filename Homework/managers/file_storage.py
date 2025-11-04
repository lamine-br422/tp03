import json
from typing import List, Optional
from pathlib import Path

class FileStorage:
    """SRP: Handles file storage operations - DIP abstraction"""
    
    def __init__(self, filename: str):
        self.filename = filename
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        if not Path(self.filename).exists():
            with open(self.filename, 'w') as f:
                json.dump([], f)
    
    def save(self, data: dict, key_field: str):
        """Save or update a record"""
        records = self.load_all()
        
        # Check if record exists and update it
        for i, record in enumerate(records):
            if record.get(key_field) == data.get(key_field):
                records[i] = data
                self._write(records)
                return
        
        # Add new record
        records.append(data)
        self._write(records)
    
    def load_all(self) -> List[dict]:
        """Load all records"""
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def find_by_field(self, field: str, value) -> Optional[dict]:
        """Find a record by field value"""
        records = self.load_all()
        for record in records:
            if record.get(field) == value:
                return record
        return None
    
    def find_all_by_field(self, field: str, value) -> List[dict]:
        """Find all records by field value"""
        records = self.load_all()
        return [r for r in records if r.get(field) == value]
    
    def delete(self, key_field: str, value):
        """Delete a record"""
        records = self.load_all()
        records = [r for r in records if r.get(key_field) != value]
        self._write(records)
    
    def _write(self, data: List[dict]):
        """Write data to file"""
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=2)
