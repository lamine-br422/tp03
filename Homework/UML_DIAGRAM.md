# UML Class Diagram - SOLID Architecture

## Madrassa Quaranic Project - After SOLID Refactoring

\`\`\`
┌─────────────────────────────────────────────────────────────────────┐
│                          SOLID ARCHITECTURE                         │
└─────────────────────────────────────────────────────────────────────┘

╔════════════════════════════════════════════════════════════════════════╗
║                         BASE CLASSES (Data)                           ║
╚════════════════════════════════════════════════════════════════════════╝

    ┌──────────────────────────┐
    │       <<abstract>>        │
    │        Member            │
    ├──────────────────────────┤
    │ - full_name: str         │
    │ - email: str             │
    │ - phone: str             │
    │ - address: str           │
    │ - join_date: date        │
    │ - skills: List[str]      │
    │ - interests: List[str]   │
    ├──────────────────────────┤
    │ + add_skill()            │
    │ + add_interest()         │
    │ + display(): str         │
    │ + to_dict(): dict        │
    └──────────────┬───────────┘
                   │
        ┌──────────┴──────────┐
        │                     │
    ┌───▼──────────┐    ┌────▼──────────┐
    │    Student   │    │    Teacher    │
    ├──────────────┤    ├───────────────┤
    │ - student_id │    │ - teacher_id  │
    │ - sub_status │    │               │
    ├──────────────┤    ├───────────────┤
    │ + display()  │    │ + display()   │
    │ + check_sub()│    │ + display()   │
    └──────────────┘    │ + assign_*()  │
                        └───────────────┘


╔════════════════════════════════════════════════════════════════════════╗
║                    EVENT HIERARCHY (OCP - Open/Closed)               ║
╚════════════════════════════════════════════════════════════════════════╝

    ┌──────────────────────────┐
    │      <<abstract>>         │
    │        Event             │
    ├──────────────────────────┤
    │ - event_name: str        │
    │ - description: str       │
    │ - event_date: date       │
    │ - organizers: List       │
    ├──────────────────────────┤
    │ + display(): str         │
    │ + get_event_type(): str  │
    │ + describe(): str        │
    └──────────────┬───────────┘
                   │
     ┌─────────────┼─────────────┐
     │             │             │
  ┌──▼────┐  ┌─────▼────┐  ┌────▼──────┐
  │ Trip  │  │ Meeting  │  │Competition│
  ├───────┤  ├──────────┤  ├───────────┤
  │ - dst │  │ - room   │  │ - prize   │
  ├───────┤  ├──────────┤  ├───────────┤
  │ +..() │  │ +..()    │  │ +..()     │
  └───────┘  └──────────┘  └───────────┘


╔════════════════════════════════════════════════════════════════════════╗
║                  SUBSCRIPTION HIERARCHY (OCP)                         ║
╚════════════════════════════════════════════════════════════════════════╝

    ┌──────────────────────────────┐
    │    <<abstract>>              │
    │    Subscription              │
    ├──────────────────────────────┤
    │ - name: str                  │
    │ - price: float               │
    │ - duration_months: int       │
    ├──────────────────────────────┤
    │ + get_duration(): str        │
    │ + display(): str             │
    └──────────────┬───────────────┘
                   │
     ┌─────────────┼─────────────┐
     │             │             │
  ┌──▼────┐  ┌─────▼────┐  ┌────▼────────┐
  │Donation│  │  Monthly │  │   Annual    │
  └────────┘  │Sub.      │  │ Sub.        │
              └──────────┘  └─────────────┘


╔════════════════════════════════════════════════════════════════════════╗
║                 INTERFACES (ISP - Interface Segregation)              ║
╚════════════════════════════════════════════════════════════════════════╝

    ┌────────────────────┐    ┌────────────────────┐
    │ <<interface>>       │    │ <<interface>>      │
    │   Payable          │    │  Organizable       │
    ├────────────────────┤    ├────────────────────┤
    │ + process_payment()│    │ + schedule()       │
    │   : bool           │    │ + add_organizer()  │
    └────────────────────┘    └────────────────────┘
           ▲                           ▲
           │                           │
      ┌────┴────┐                ┌────┴────┐
      │          │                │         │
  Donation   Subscription      Event   Competition


╔════════════════════════════════════════════════════════════════════════╗
║           MANAGERS & REPOSITORIES (SRP - Single Responsibility)      ║
╚════════════════════════════════════════════════════════════════════════╝

    ┌────────────────────────────┐
    │    StorageInterface        │
    │      (Abstract)            │
    ├────────────────────────────┤
    │ + save(data): bool         │
    │ + load(): dict             │
    │ + delete(): bool           │
    └────────┬───────────────────┘
             │
      ┌──────┴──────┐
      │             │
  ┌───▼──────┐  ┌──▼────────┐
  │FileStorage│  │JSONStorage│
  └───────────┘  └───────────┘

    
    Repositories (Using Storage):
    ┌──────────────────────────────┐
    │  MemberRepository            │
    │ - storage: StorageInterface  │
    ├──────────────────────────────┤
    │ + save_member()              │
    │ + load_members()             │
    └──────────────────────────────┘
    
    ┌──────────────────────────────┐
    │   EventManager               │
    │ - storage: StorageInterface  │
    ├──────────────────────────────┤
    │ + create_event()             │
    │ + list_events()              │
    └──────────────────────────────┘

    ┌──────────────────────────────┐
    │  FinanceManager              │
    │ - storage: StorageInterface  │
    ├──────────────────────────────┤
    │ + process_payment()          │
    │ + generate_report()          │
    └──────────────────────────────┘


╔════════════════════════════════════════════════════════════════════════╗
║         DEPENDENCY INJECTION (DIP - Dependency Inversion)             ║
╚════════════════════════════════════════════════════════════════════════╝

    ┌─────────────────────────────────────────┐
    │        Application Main                 │
    ├─────────────────────────────────────────┤
    │ - storage: StorageInterface             │
    │ - member_repo: MemberRepository         │
    │ - event_mgr: EventManager               │
    │ - finance_mgr: FinanceManager           │
    ├─────────────────────────────────────────┤
    │ Dependencies injected, not tightly      │
    │ coupled. Can switch storage backends    │
    │ without changing managers               │
    └─────────────────────────────────────────┘
           ▲
           │ depends on abstraction
           │
    ┌──────┴──────────────────┐
    │  StorageInterface       │
    │  (JSON, File, DB, etc)  │
    └────────────────────────┘


╔════════════════════════════════════════════════════════════════════════╗
║                        DESIGN PATTERNS USED                           ║
╚════════════════════════════════════════════════════════════════════════╝

1. Abstract Base Classes (ABC) - For LSP compliance
2. Dependency Injection - For DIP compliance
3. Repository Pattern - For SRP (separating data access)
4. Strategy Pattern - For storage implementations
5. Factory Pattern - For creating different event types
\`\`\`

---

## Legend

- **Abstract Classes**: Defined with `ABC` module
- **Interfaces**: Protocol-like behavior, implemented by multiple classes
- **Inheritance**: Parent ← Child relationship
- **Dependency**: Uses/Depends on

---

## Key SOLID Principles Implementation

| Principle | Implementation | Benefit |
|-----------|-----------------|---------|
| **SRP** | Repositories handle data access | Each class has single responsibility |
| **OCP** | Event subclasses, Subscription subclasses | Can add new types without modifying base |
| **LSP** | All Event subclasses valid Event replacements | Code using Event works with any subclass |
| **ISP** | Payable, Organizable interfaces | Classes implement only needed methods |
| **DIP** | Managers depend on StorageInterface | Can swap storage without changing managers |
