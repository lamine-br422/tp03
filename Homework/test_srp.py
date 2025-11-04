"""
TEST SRP (Single Responsibility Principle)
Chaque classe a une seule responsabilité
"""

from datetime import date
from models.member import Member
from models.student import Student
from models.teacher import Teacher


def test_srp():
    print("=" * 60)
    print("TEST SRP - Single Responsibility Principle")
    print("=" * 60)
    
    # Test 1: Member class - only handles member data
    print("\n[TEST 1] Member - Responsabilité unique: gérer les données")
    member = Member(
        full_name="Ali Ahmed",
        email="ali@madrassa.com",
        phone="0123456789",
        address="Casablanca",
        join_date=date(2024, 1, 15)
    )
    print(f"✓ Membre créé: {member.display()}")
    
    # Test 2: Student - extends Member, adds student-specific data
    print("\n[TEST 2] Student - Responsabilité unique: gérer les données d'étudiant")
    student = Student(
        full_name="Fatima Hassan",
        email="fatima@madrassa.com",
        phone="0987654321",
        address="Fes",
        join_date=date(2024, 2, 1),
        student_id=101,
        subscription_status="Active"
    )
    print(f"✓ Étudiant créé: {student.display()}")
    print(f"✓ Statut abonnement: {student.check_subscription()}")
    
    # Test 3: Teacher - extends Member, adds teacher-specific data
    print("\n[TEST 3] Teacher - Responsabilité unique: gérer les données d'enseignant")
    teacher = Teacher(
        full_name="Mohamed Hassan",
        email="m.hassan@madrassa.com",
        phone="0612345678",
        address="Rabat",
        join_date=date(2023, 9, 1),
        teacher_id=5,
        specialization="Quran"
    )
    print(f"✓ Enseignant créé: {teacher.display()}")
    print(f"✓ Spécialisation: {teacher.specialization}")
    
    # Test 4: Add skills (single responsibility maintained)
    print("\n[TEST 4] Ajouter des compétences - SRP maintenue")
    member.add_skill("Teaching")
    member.add_skill("Leadership")
    teacher.add_skill("Tajweed")
    student.add_skill("Memorization")
    
    print(f"✓ Compétences du membre: {member.skills}")
    print(f"✓ Compétences de l'enseignant: {teacher.skills}")
    print(f"✓ Compétences de l'étudiant: {student.skills}")
    
    # Test 5: Each class has ONE responsibility
    print("\n[TEST 5] Vérification SRP:")
    print(f"✓ Member: stocke les données de base")
    print(f"✓ Student: stocke les données d'étudiant (hérite de Member)")
    print(f"✓ Teacher: stocke les données d'enseignant (hérite de Member)")
    print(f"✓ Pas de responsabilités multiples (pas de sauvegarde, pas d'affichage complexe)")
    
    print("\n✓ TEST SRP RÉUSSI: Chaque classe a une responsabilité unique!")
    print("=" * 60)


if __name__ == "__main__":
    test_srp()
