from models.member import Member
from managers.file_storage import FileStorage

class MemberRepository:
    """SRP: Manages member persistence - DIP uses abstraction"""
    
    def __init__(self, filename: str):
        self.storage = FileStorage(filename)
    
    def save_member(self, member: Member):
        """Save member to storage"""
        self.storage.save(member.to_dict(), 'email')
    
    def find_by_email(self, email: str) -> Member:
        """Find member by email"""
        data = self.storage.find_by_field('email', email)
        if data:
            return Member.from_dict(data)
        return None
    
    def load_all_members(self) -> list:
        """Load all members"""
        return [Member.from_dict(data) for data in self.storage.load_all()]
    
    def delete_member(self, email: str):
        """Delete member by email"""
        self.storage.delete('email', email)
