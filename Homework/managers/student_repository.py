from datetime import date
from models.student import Student
from managers.file_storage import FileStorage

class StudentRepository:
    """SRP: Manages student persistence - specialized repository for students"""
    
    def __init__(self, filename: str):
        self.storage = FileStorage(filename)
    
    def save_student(self, student: Student):
        """Save student to storage"""
        self.storage.save(student.to_dict(), 'student_id')
    
    def find_by_id(self, student_id: int) -> Student:
        """Find student by ID"""
        data = self.storage.find_by_field('student_id', student_id)
        if data:
            return Student.from_dict(data)
        return None
    
    def find_by_email(self, email: str) -> Student:
        """Find student by email"""
        data = self.storage.find_by_field('email', email)
        if data:
            return Student.from_dict(data)
        return None
    
    def find_by_subscription_status(self, status: str) -> list:
        """Find all students with specific subscription status"""
        data_list = self.storage.find_all_by_field('subscription_status', status)
        return [Student.from_dict(data) for data in data_list]
    
    def load_all_students(self) -> list:
        """Load all students"""
        return [Student.from_dict(data) for data in self.storage.load_all()]
    
    def delete_student(self, student_id: int):
        """Delete student by ID"""
        self.storage.delete('student_id', student_id)
