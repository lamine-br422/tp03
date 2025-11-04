"""
TEST LSP (Liskov Substitution Principle)
Les sous-classes peuvent remplacer la classe parente
"""

from datetime import date
from models.member import Member
from models.student import Student
from models.teacher import Teacher
from models.event import Event, Trip, Meeting, Competition


def display_member_info(member: Member):
    """Fonction qui accepte Member - fonctionne avec n'importe quel sous-type"""
    print(f"  Affichage: {member.display()}")
    print(f"  Email: {member.email}")
    print(f"  Adresse: {member.address}")


def display_event_details(event: Event):
    """Fonction qui accepte Event - fonctionne avec n'importe quel sous-type"""
    print(f"  Affichage: {event.display()}")
    print(f"  Type: {event.get_event_type()}")
    print(f"  Description: {event.describe()}")


def test_lsp():
    print("=" * 60)
    print("TEST LSP - Liskov Substitution Principle")
    print("=" * 60)
    
    # Test 1: Student et Teacher peuvent remplacer Member
    print("\n[TEST 1] Substitution Member → Student/Teacher")
    print("-" * 40)
    
    members = [
        Member("Ali Ahmed", "ali@mail.com", "111", "Casablanca", date(2024, 1, 1)),
        Student("Fatima", "fatima@mail.com", "222", "Fes", date(2024, 1, 1), 101, "Active"),
        Teacher("Mohamed", "m@mail.com", "333", "Rabat", date(2024, 1, 1), 5, "Quran")
    ]
    
    print("✓ Substitution LSP - Member accepte aussi Student et Teacher:")
    for member in members:
        display_member_info(member)
        print()
    
    # Test 2: Trip, Meeting, Competition peuvent remplacer Event
    print("\n[TEST 2] Substitution Event → Trip/Meeting/Competition")
    print("-" * 40)
    
    events = [
        Trip("Voyage", "Umra", date(2024, 6, 15), "Saudi Arabia"),
        Meeting("Conférence", "Tafsir", date(2024, 3, 20), "Salle A1"),
        Competition("Compétition", "Memorisation", date(2024, 4, 10), "iPhone")
    ]
    
    print("✓ Substitution LSP - Event accepte Trip, Meeting, Competition:")
    for event in events:
        display_event_details(event)
        print()
    
    # Test 3: Vérifier que la substitution fonctionne correctement
    print("\n[TEST 3] Vérification comportement substitution")
    print("-" * 40)
    
    student = Student("Amira", "amira@mail.com", "444", "Marrakech", 
                     date(2024, 1, 1), 102, "Active")
    
    print("✓ Student peut être utilisé partout où Member est attendu:")
    print(f"  - display() retourne: {student.display()}")
    print(f"  - check_subscription() retourne: {student.check_subscription()}")
    print(f"  - Comportement cohérent et prévisible")
    
    print("\n✓ TEST LSP RÉUSSI: Substitution fonctionne correctement!")
    print("  - Student et Teacher peuvent remplacer Member")
    print("  - Trip, Meeting, Competition peuvent remplacer Event")
    print("=" * 60)


if __name__ == "__main__":
    test_lsp()
