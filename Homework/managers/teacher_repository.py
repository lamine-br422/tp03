from datetime import date
from models.teacher import Teacher
from managers.file_storage import FileStorage

class TeacherRepository:
    """SRP: Manages teacher persistence - specialized repository for teachers"""
    
    def __init__(self, filename: str):
        self.storage = FileStorage(filename)
    
    def save_teacher(self, teacher: Teacher):
        """Save teacher to storage"""
        self.storage.save(teacher.to_dict(), 'teacher_id')
    
    def find_by_id(self, teacher_id: int) -> Teacher:
        """Find teacher by ID"""
        data = self.storage.find_by_field('teacher_id', teacher_id)
        if data:
            return Teacher.from_dict(data)
        return None
    
    def find_by_email(self, email: str) -> Teacher:
        """Find teacher by email"""
        data = self.storage.find_by_field('email', email)
        if data:
            return Teacher.from_dict(data)
        return None
    
    def find_by_specialization(self, specialization: str) -> list:
        """Find all teachers with a specific specialization"""
        data_list = self.storage.find_all_by_field('specialization', specialization)
        return [Teacher.from_dict(data) for data in data_list]
    
    def load_all_teachers(self) -> list:
        """Load all teachers"""
        return [Teacher.from_dict(data) for data in self.storage.load_all()]
    
    def delete_teacher(self, teacher_id: int):
        """Delete teacher by ID"""
        self.storage.delete('teacher_id', teacher_id)
