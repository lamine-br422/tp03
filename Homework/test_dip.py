"""
TEST DIP (Dependency Inversion Principle)
Les modules dépendent d'abstractions, pas de classes concrètes
"""

from abc import ABC, abstractmethod
from datetime import date
from typing import List


class StorageInterface(ABC):
    """Abstraction pour la persistance"""
    @abstractmethod
    def save(self, data: dict) -> str:
        pass
    
    @abstractmethod
    def load(self, key: str) -> dict:
        pass


class NotificationInterface(ABC):
    """Abstraction pour les notifications"""
    @abstractmethod
    def send(self, message: str) -> str:
        pass


class FileStorage(StorageInterface):
    """Implémentation FileStorage - détail d'implémentation"""
    
    def save(self, data: dict) -> str:
        return f"[FILE] Données sauvegardées dans un fichier: {data}"
    
    def load(self, key: str) -> dict:
        return {"source": "file", "data": key}


class DatabaseStorage(StorageInterface):
    """Implémentation DatabaseStorage - détail d'implémentation"""
    
    def save(self, data: dict) -> str:
        return f"[DATABASE] Données sauvegardées en base de données: {data}"
    
    def load(self, key: str) -> dict:
        return {"source": "database", "data": key}


class EmailNotification(NotificationInterface):
    """Implémentation EmailNotification - détail d'implémentation"""
    
    def send(self, message: str) -> str:
        return f"[EMAIL] Message envoyé par email: {message}"


class SMSNotification(NotificationInterface):
    """Implémentation SMSNotification - détail d'implémentation"""
    
    def send(self, message: str) -> str:
        return f"[SMS] Message envoyé par SMS: {message}"


class PushNotification(NotificationInterface):
    """Implémentation PushNotification - détail d'implémentation"""
    
    def send(self, message: str) -> str:
        return f"[PUSH] Notification push envoyée: {message}"


class StudentManager:
    """Manager qui dépend d'abstractions (DIP compliant)"""
    
    def __init__(self, storage: StorageInterface, notification: NotificationInterface):
        # Dépend d'interfaces abstraites, pas d'implémentations concrètes
        self.storage = storage
        self.notification = notification
    
    def register_student(self, student_name: str, email: str) -> str:
        student_data = {
            'name': student_name,
            'email': email,
            'date': str(date.today())
        }
        
        # Utiliser l'abstraction storage
        storage_msg = self.storage.save(student_data)
        
        # Utiliser l'abstraction notification
        notify_msg = self.notification.send(f"Nouvel étudiant: {student_name}")
        
        return f"✓ {storage_msg}\n✓ {notify_msg}"


def test_dip():
    print("=" * 60)
    print("TEST DIP - Dependency Inversion Principle")
    print("=" * 60)
    
    # Test 1: StudentManager avec FileStorage et EmailNotification
    print("\n[TEST 1] StudentManager + FileStorage + EmailNotification")
    print("-" * 40)
    manager1 = StudentManager(FileStorage(), EmailNotification())
    result1 = manager1.register_student("Ali Ahmed", "ali@mail.com")
    print(result1)
    
    # Test 2: StudentManager avec DatabaseStorage et SMSNotification
    print("\n[TEST 2] StudentManager + DatabaseStorage + SMSNotification")
    print("-" * 40)
    manager2 = StudentManager(DatabaseStorage(), SMSNotification())
    result2 = manager2.register_student("Fatima Hassan", "fatima@mail.com")
    print(result2)
    
    # Test 3: StudentManager avec FileStorage et PushNotification
    print("\n[TEST 3] StudentManager + FileStorage + PushNotification")
    print("-" * 40)
    manager3 = StudentManager(FileStorage(), PushNotification())
    result3 = manager3.register_student("Amira Ahmed", "amira@mail.com")
    print(result3)
    
    # Test 4: Démontrer la flexibilité
    print("\n[TEST 4] Flexibilité du système (Injection de dépendance)")
    print("-" * 40)
    print("✓ StudentManager peut accepter TOUTE implémentation de StorageInterface")
    print("✓ StudentManager peut accepter TOUTE implémentation de NotificationInterface")
    print("✓ Ajouter une nouvelle implémentation ne change pas StudentManager")
    print("✓ C'est ça le DIP: dépendre d'abstractions, pas de détails d'implémentation")
    
    print("\n✓ TEST DIP RÉUSSI: Dépendances inversées correctement!")
    print("  - StudentManager dépend de StorageInterface et NotificationInterface")
    print("  - Les implémentations (File, Database, Email, SMS, Push) sont interchangeables")
    print("  - Nouvelles implémentations sans modifier StudentManager")
    print("=" * 60)


if __name__ == "__main__":
    test_dip()
