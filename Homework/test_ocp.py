"""
TEST OCP (Open/Closed Principle)
Classes ouvertes à l'extension, fermées à la modification
"""

from datetime import date
from models.event import Event, Trip, Meeting, Competition
from models.subscription import (
    Subscription, 
    Donation, 
    MonthlySubscription, 
    AnnualSubscription
)


def test_ocp_events():
    print("\n[TEST OCP - EVENTS]")
    print("-" * 40)
    
    # Créer différents types d'événements SANS modifier la classe Event
    trip = Trip(
        event_name="Voyage Umra",
        description="Voyage éducatif à La Mecque",
        event_date=date(2024, 6, 15),
        destination="Saudi Arabia"
    )
    
    meeting = Meeting(
        event_name="Conférence Quranique",
        description="Discussion sur le Tafsir",
        event_date=date(2024, 3, 20),
        room="Salle A1"
    )
    
    competition = Competition(
        event_name="Compétition Mémorisation",
        description="Compétition de mémorisation du Coran",
        event_date=date(2024, 4, 10),
        prize="iPhone 15"
    )
    
    events = [trip, meeting, competition]
    
    print("✓ Événements créés SANS modifier Event (Open for extension):")
    for event in events:
        print(f"  - {event.display()}")
        print(f"    Type: {event.get_event_type()}")
        print(f"    Description: {event.describe()}\n")


def test_ocp_subscriptions():
    print("\n[TEST OCP - SUBSCRIPTIONS]")
    print("-" * 40)
    
    # Créer différents types d'abonnement SANS modifier la classe Subscription
    std_sub = Subscription(
        student_id=101,
        amount=50.0,
        date_sub=date(2024, 1, 1)
    )
    
    donation = Donation(
        student_id=102,
        amount=100.0,
        date_sub=date(2024, 1, 5),
        donor_name="Ahmed Al-Khouri"
    )
    
    monthly = MonthlySubscription(
        student_id=103,
        amount=20.0,
        date_sub=date(2024, 1, 10)
    )
    
    annual = AnnualSubscription(
        student_id=104,
        amount=200.0,
        date_sub=date(2024, 1, 15),
        discount=0.15
    )
    
    subscriptions = [std_sub, donation, monthly, annual]
    
    print("✓ Abonnements créés SANS modifier Subscription (Open for extension):")
    for sub in subscriptions:
        print(f"  - {sub.display()}")
        print(f"    Type: {sub.get_subscription_type()}\n")


def test_ocp():
    print("=" * 60)
    print("TEST OCP - Open/Closed Principle")
    print("=" * 60)
    
    test_ocp_events()
    test_ocp_subscriptions()
    
    print("\n✓ TEST OCP RÉUSSI: Nouvelles classes sans modifier l'existant!")
    print("  - Event ouvert à Trip, Meeting, Competition")
    print("  - Subscription ouvert à Donation, Monthly, Annual")
    print("=" * 60)


if __name__ == "__main__":
    test_ocp()
