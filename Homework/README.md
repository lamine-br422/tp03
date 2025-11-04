# Homework – School Management System (Madrassa)

Applying SOLID principles to the management of a Quran school (Madrassa).

---

## ✅ SRP – Single Responsibility Principle

**Where applied**  
- `Member` now only manages personal information  
- A new manager class is used to load/save data instead of `Member`

**Problem solved**  
➡️ Avoided mixing data logic and file/storage logic in one class

---

## ✅ OCP – Open / Closed Principle

**Where applied**  
- Subscription system now supports extensions:
  - `Donation`
  - `MonthlySubscription`
  - `AnnualSubscription`

**Problem solved**  
➡️ New payment types added without modifying existing subscription logic

---

## ✅ LSP – Liskov Substitution Principle

**Where applied**  
- All classes derived from `Event` behave correctly when used as a base object
- Display function works for all event types

**Problem solved**  
➡️ Calling `display_event_details(event)` works with any subclass (`Meeting`, `Competition`, `Trip`)

---

## ✅ ISP – Interface Segregation Principle

**Where applied**  
- Created small interfaces:
  - `Payable` → process_payment()
  - `Organizable` → schedule()
  - `Registrable` → register_member()

**Problem solved**  
➡️ Avoided forcing a class to implement methods it doesn’t use  
➡️ Example: `Donation` only handles payments, not member registration

---

## ✅ DIP – Dependency Inversion Principle

**Where applied**  
- Storage is injected instead of hard-coded:
  - `CSVStorage`
  - `JSONStorage`
  - `DatabaseStorage`

**Problem solved**  
➡️ Application logic does not depend on a specific data storage  
➡️ Easy to switch storage without modifying business logic

---

## 📌 Project Structure

