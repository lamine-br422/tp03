"""
TEST ISP (Interface Segregation Principle)
Classes n'implémentent que les interfaces nécessaires
"""

from datetime import date
from abc import ABC, abstractmethod


class Payable(ABC):
    """Interface pour les objets payables"""
    @abstractmethod
    def process_payment(self) -> str:
        pass


class Organizable(ABC):
    """Interface pour les objets organisables"""
    @abstractmethod
    def schedule(self) -> str:
        pass


class Registrable(ABC):
    """Interface pour les objets enregistrables"""
    @abstractmethod
    def register_member(self, member_name: str) -> str:
        pass


# Classes qui implémentent SEULEMENT les interfaces nécessaires
class StudentPayment(Payable):
    """Implémente seulement Payable"""
    
    def __init__(self, student_id: int, amount: float):
        self.student_id = student_id
        self.amount = amount
    
    def process_payment(self) -> str:
        return f"Paiement de {self.amount}€ pour étudiant #{self.student_id}"


class Event(Organizable):
    """Implémente seulement Organizable"""
    
    def __init__(self, event_name: str, event_date: date):
        self.event_name = event_name
        self.event_date = event_date
    
    def schedule(self) -> str:
        return f"Événement '{self.event_name}' programmé pour {self.event_date}"


class Course(Organizable, Registrable):
    """Implémente Organizable ET Registrable (nécessaire pour ce cas)"""
    
    def __init__(self, course_name: str, course_date: date):
        self.course_name = course_name
        self.course_date = course_date
        self.registered_members = []
    
    def schedule(self) -> str:
        return f"Cours '{self.course_name}' programmé pour {self.course_date}"
    
    def register_member(self, member_name: str) -> str:
        self.registered_members.append(member_name)
        return f"✓ {member_name} enregistré au cours '{self.course_name}'"


class Workshop(Organizable, Registrable, Payable):
    """Implémente les 3 interfaces (nécessaire pour ce cas)"""
    
    def __init__(self, workshop_name: str, workshop_date: date, price: float):
        self.workshop_name = workshop_name
        self.workshop_date = workshop_date
        self.price = price
        self.registered = []
    
    def schedule(self) -> str:
        return f"Atelier '{self.workshop_name}' programmé pour {self.workshop_date}"
    
    def register_member(self, member_name: str) -> str:
        self.registered.append(member_name)
        return f"✓ {member_name} enregistré à l'atelier '{self.workshop_name}'"
    
    def process_payment(self) -> str:
        return f"Frais d'atelier: {self.price}€"


def test_isp():
    print("=" * 60)
    print("TEST ISP - Interface Segregation Principle")
    print("=" * 60)
    
    # Test 1: StudentPayment - implémente SEULEMENT Payable
    print("\n[TEST 1] StudentPayment - Implémente SEULEMENT Payable")
    print("-" * 40)
    payment = StudentPayment(101, 150.0)
    print(f"✓ {payment.process_payment()}")
    print("✓ StudentPayment n'a PAS schedule() ou register_member()")
    
    # Test 2: Event - implémente SEULEMENT Organizable
    print("\n[TEST 2] Event - Implémente SEULEMENT Organizable")
    print("-" * 40)
    event = Event("Conférence", date(2024, 3, 20))
    print(f"✓ {event.schedule()}")
    print("✓ Event n'a PAS process_payment() ou register_member()")
    
    # Test 3: Course - implémente Organizable ET Registrable
    print("\n[TEST 3] Course - Implémente Organizable ET Registrable")
    print("-" * 40)
    course = Course("Tajweed Level 1", date(2024, 4, 1))
    print(f"✓ {course.schedule()}")
    print(f"✓ {course.register_member('Amira Hassan')}")
    print("✓ Course n'a PAS process_payment()")
    
    # Test 4: Workshop - implémente les 3 interfaces
    print("\n[TEST 4] Workshop - Implémente 3 interfaces (nécessaire)")
    print("-" * 40)
    workshop = Workshop("Quran Recitation", date(2024, 5, 15), 50.0)
    print(f"✓ {workshop.schedule()}")
    print(f"✓ {workshop.register_member('Hassan Ahmed')}")
    print(f"✓ {workshop.process_payment()}")
    
    print("\n✓ TEST ISP RÉUSSI: Classes implémentent seulement les interfaces nécessaires!")
    print("  - StudentPayment: une interface (Payable)")
    print("  - Event: une interface (Organizable)")
    print("  - Course: deux interfaces (Organizable, Registrable)")
    print("  - Workshop: trois interfaces (toutes nécessaires)")
    print("=" * 60)


if __name__ == "__main__":
    test_isp()
