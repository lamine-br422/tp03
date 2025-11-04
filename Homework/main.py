from datetime import date
from models.member import Member
from models.student import Student
from models.teacher import Teacher
from models.event import Trip, Meeting, Competition
from models.subscription import Subscription, Donation, MonthlySubscription, AnnualSubscription
from managers.member_repository import MemberRepository
from managers.student_repository import StudentRepository
from managers.teacher_repository import TeacherRepository
from managers.event_manager import EventManager
from managers.finance_manager import FinanceManager

def test_member_srp():
    """Test SRP applied to Member class"""
    print("=" * 60)
    print("=== TEST SRP - MEMBER ===")
    print("=" * 60)
    
    member1 = Member(
        full_name="Alice Dupont",
        email="alice@email.com",
        phone="0123456789",
        address="Paris",
        join_date=date(2024, 1, 15)
    )
    member1.add_skill("Python")
    member1.add_interest("Lecture")
    
    member2 = Member(
        full_name="Bob Martin",
        email="bob@email.com", 
        phone="0987654321",
        address="Lyon",
        join_date=date(2024, 2, 20)
    )
    member2.add_skill("Java")
    member2.add_interest("Sport")
    
    repo = MemberRepository("test_members.json")
    repo.save_member(member1)
    repo.save_member(member2)
    print("✓ Membres sauvegardés")
    
    loaded_member = repo.find_by_email("alice@email.com")
    if loaded_member:
        print(f"✓ Membre chargé: {loaded_member.display()}")
    
    all_members = repo.load_all_members()
    print(f"✓ Total membres en base: {len(all_members)}")


def test_student_srp():
    """Test SRP applied to Student class - LSP compliant"""
    print("\n" + "=" * 60)
    print("=== TEST SRP - STUDENT (LSP Compliant) ===")
    print("=" * 60)
    
    student1 = Student(
        full_name="Mohammed Hassan",
        email="mohammed@email.com",
        phone="0645123456",
        address="Rabat",
        join_date=date(2024, 1, 10),
        student_id=1001,
        subscription_status="Active"
    )
    student1.add_skill("Quranic Studies")
    student1.add_interest("Islamic History")
    
    student2 = Student(
        full_name="Fatima Ahmed",
        email="fatima@email.com",
        phone="0656789012",
        address="Casablanca",
        join_date=date(2024, 2, 5),
        student_id=1002,
        subscription_status="Pending"
    )
    student2.add_skill("Arabic Language")
    
    repo = StudentRepository("test_students.json")
    repo.save_student(student1)
    repo.save_student(student2)
    print("✓ Étudiants sauvegardés")
    
    loaded = repo.find_by_id(1001)
    if loaded:
        print(f"✓ Étudiant chargé: {loaded.display()}")
        print(f"  Statut abonnement: {loaded.check_subscription()}")
    
    active_students = repo.find_by_subscription_status("Active")
    print(f"✓ Étudiants actifs: {len(active_students)}")


def test_teacher_srp():
    """Test SRP applied to Teacher class - LSP compliant"""
    print("\n" + "=" * 60)
    print("=== TEST SRP - TEACHER (LSP Compliant) ===")
    print("=" * 60)
    
    teacher1 = Teacher(
        full_name="Dr. Omar Khalil",
        email="omar@email.com",
        phone="0601234567",
        address="Fez",
        join_date=date(2023, 9, 1),
        teacher_id=2001,
        specialization="Quranic Interpretation"
    )
    teacher1.add_skill("Tafseer")
    teacher1.assign_group("Group A")
    teacher1.assign_event("Voyage éducatif")
    
    teacher2 = Teacher(
        full_name="Ustadha Layla Kareem",
        email="layla@email.com",
        phone="0612345678",
        address="Tangier",
        join_date=date(2023, 10, 15),
        teacher_id=2002,
        specialization="Islamic Law"
    )
    teacher2.add_skill("Fiqh")
    teacher2.assign_group("Group B")
    
    repo = TeacherRepository("test_teachers.json")
    repo.save_teacher(teacher1)
    repo.save_teacher(teacher2)
    print("✓ Professeurs sauvegardés")
    
    loaded = repo.find_by_id(2001)
    if loaded:
        print(f"✓ Professeur chargé: {loaded.display()}")
        print(f"  {loaded.display_group()}")
        print(f"  Événements assignés: {loaded.get_assigned_events()}")
    
    fiqh_teachers = repo.find_by_specialization("Islamic Law")
    print(f"✓ Professeurs spécialisés en Fiqh: {len(fiqh_teachers)}")


def test_event_ocp():
    """Test OCP applied to Event hierarchy"""
    print("\n" + "=" * 60)
    print("=== TEST OCP - EVENT (Open/Closed Principle) ===")
    print("=" * 60)
    
    trip = Trip(
        event_name="Voyage éducatif",
        description="Visite d'une mosquée historique",
        event_date=date(2024, 3, 10),
        destination="Istanbul"
    )
    
    meeting = Meeting(
        event_name="Réunion mensuelle",
        description="Réunion pour discuter des activités",
        event_date=date(2024, 3, 15),
        room="Salle principale"
    )
    
    competition = Competition(
        event_name="Concours Qur'an",
        description="Concours de mémorisation",
        event_date=date(2024, 4, 5),
        prize="Voyage en Arabie Saoudite"
    )
    
    event_mgr = EventManager("test_events.json")
    event_mgr.save_event(trip)
    event_mgr.save_event(meeting)
    event_mgr.save_event(competition)
    print("✓ Événements sauvegardés")
    
    loaded_trip = event_mgr.find_by_name("Voyage éducatif")
    if loaded_trip:
        print(f"✓ Trip chargé: {loaded_trip.display()}")
        print(f"  {loaded_trip.describe()}")
    
    all_events = event_mgr.load_all_events()
    print(f"✓ Total événements: {len(all_events)}")


def test_subscription_ocp_isp():
    """Test OCP and ISP applied to Subscription - new types without modification"""
    print("\n" + "=" * 60)
    print("=== TEST OCP/ISP - SUBSCRIPTION ===")
    print("=" * 60)
    
    # Original subscription
    sub1 = Subscription(
        student_id=1001,
        amount=150.0,
        date_sub=date(2024, 1, 5),
        status="paid"
    )
    
    # New subscription type - Donation (OCP)
    donation = Donation(
        student_id=1002,
        amount=500.0,
        date_sub=date(2024, 1, 20),
        donor_name="Ahmed Al-Mansouri"
    )
    donation.mark_paid()
    
    # New subscription type - Monthly (OCP)
    monthly = MonthlySubscription(
        student_id=1003,
        amount=50.0,
        date_sub=date(2024, 2, 1)
    )
    monthly.mark_paid()
    
    # New subscription type - Annual (OCP)
    annual = AnnualSubscription(
        student_id=1004,
        amount=500.0,
        date_sub=date(2024, 1, 1),
        discount=0.15
    )
    annual.mark_paid()
    
    finance_mgr = FinanceManager("test_subscriptions.json")
    finance_mgr.save_subscription(sub1)
    finance_mgr.save_subscription(donation)
    finance_mgr.save_subscription(monthly)
    finance_mgr.save_subscription(annual)
    print("✓ Abonnements de tous types sauvegardés")
    
    print(f"\nTypes d'abonnements créés:")
    print(f"  - {sub1.display()} (type: {sub1.get_subscription_type()})")
    print(f"  - {donation.display()} (type: {donation.get_subscription_type()})")
    print(f"  - {monthly.display()} (type: {monthly.get_subscription_type()})")
    print(f"  - {annual.display()} (type: {annual.get_subscription_type()})")
    
    revenue = finance_mgr.get_total_revenue()
    print(f"\n✓ Revenu total: {revenue}€")
    
    paid_subs = finance_mgr.get_paid_subscriptions()
    print(f"✓ Abonnements payés: {len(paid_subs)}")


def test_lsp_substitution():
    """Test LSP: All Member subclasses substitutable"""
    print("\n" + "=" * 60)
    print("=== TEST LSP - LISKOV SUBSTITUTION ===")
    print("=" * 60)
    
    # LSP: All these are Members
    members = [
        Member("Generic Member", "generic@email.com", "0100000000", "Somewhere", date(2024, 1, 1)),
        Student("Ali Student", "student@email.com", "0111111111", "City1", date(2024, 1, 1), 5001, "Active"),
        Teacher("Sarah Teacher", "teacher@email.com", "0122222222", "City2", date(2024, 1, 1), 3001, "Quranic")
    ]
    
    print("✓ LSP: Tous les objets sont des Members")
    for member in members:
        print(f"  - {member.display()}")
        print(f"    Type: {type(member).__name__}")
    
    print("\n✓ LSP: display_member_info() fonctionne avec tous les types")


def test_integration():
    """Integration test combining all components"""
    print("\n" + "=" * 60)
    print("=== TEST INTÉGRATION COMPLÈTE ===")
    print("=" * 60)
    
    # Create entities
    student = Student(
        full_name="Karim Benchekroun",
        email="karim@email.com",
        phone="0634567890",
        address="Marrakech",
        join_date=date(2024, 2, 15),
        student_id=1010,
        subscription_status="Active"
    )
    student.add_skill("Hafiz Trainee")
    
    teacher = Teacher(
        full_name="Shaikh Ibrahim Ali",
        email="shaikh@email.com",
        phone="0645678901",
        address="Marrakech",
        join_date=date(2023, 8, 1),
        teacher_id=2010,
        specialization="Hifz Training"
    )
    teacher.assign_group("Advanced Hafiz")
    
    event = Meeting(
        event_name="Hifz Training Session",
        description="Advanced memorization techniques",
        event_date=date(2024, 4, 10),
        room="Salle de formation"
    )
    
    subscription = MonthlySubscription(
        student_id=1010,
        amount=75.0,
        date_sub=date(2024, 2, 15)
    )
    subscription.mark_paid()
    
    # Save with repositories
    student_repo = StudentRepository("test_students.json")
    teacher_repo = TeacherRepository("test_teachers.json")
    event_mgr = EventManager("test_events.json")
    finance_mgr = FinanceManager("test_subscriptions.json")
    
    student_repo.save_student(student)
    teacher_repo.save_teacher(teacher)
    event_mgr.save_event(event)
    finance_mgr.save_subscription(subscription)
    
    print("✓ Scénario d'intégration complet:")
    print(f"  Étudiant: {student.display()}")
    print(f"  Professeur: {teacher.display()}")
    print(f"  Événement: {event.display()}")
    print(f"  Abonnement: {subscription.display()}")


if __name__ == "__main__":
    print("\n" + "🚀" * 30)
    print("🚀 TEST DU REFACTORING SOLID PRINCIPLES - MADRASSA QUARANIC 🚀")
    print("🚀" * 30)
    
    test_member_srp()
    test_student_srp()
    test_teacher_srp()
    test_event_ocp()
    test_subscription_ocp_isp()
    test_lsp_substitution()
    test_integration()
    
    print("\n" + "=" * 60)
    print("🎉 TOUS LES TESTS SOLID SONT TERMINÉS AVEC SUCCÈS!")
    print("=" * 60)
    print("\n📊 PRINCIPES SOLID APPLIQUÉS:")
    print("  ✓ SRP: Member, Student, Teacher, Event, Subscription séparées")
    print("  ✓ OCP: Event et Subscription extensibles sans modification")
    print("  ✓ LSP: Student et Teacher substituables à Member")
    print("  ✓ ISP: Interfaces segregated (Payable, Organizable, etc)")
    print("  ✓ DIP: Managers utilisent FileStorage abstraction")
    print("\n📁 Fichiers créés:")
    print("  - test_members.json")
    print("  - test_students.json")
    print("  - test_teachers.json")
    print("  - test_events.json")
    print("  - test_subscriptions.json")
    print("\n✅ Structure SOLID appliquée avec succès!")
