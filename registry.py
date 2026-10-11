"""
registry.py
Handles data structures and registry operations for the Healthcare System.
"""

from models import Patient, MedicalRecord

# Core Data Structure: Dictionary storing objects with unique Patient ID as key
patient_registry: dict[str, Patient] = {}


def register_patient(patient_obj: Patient) -> bool:
    """Adds a valid Patient object to the registry dictionary."""
    if not Patient.validate_patient_id(patient_obj.patient_id):
        print(f"[!] Error: Invalid ID format '{patient_obj.patient_id}'. Must be 'PAT-XXX'.")
        return False

    if patient_obj.patient_id in patient_registry:
        print(f"[!] Error: Patient ID '{patient_obj.patient_id}' is already registered.")
        return False

    patient_registry[patient_obj.patient_id] = patient_obj
    print(f"[✓] Patient '{patient_obj.patient_id}' registered successfully.")
    return True


def find_patient(patient_id: str) -> Patient | None:
    """Retrieves a Patient object from the registry dictionary by key."""
    return patient_registry.get(patient_id, None)


def display_all_patients() -> None:
    """Loops through the dictionary and outputs all registered patients."""
    print("\n" + "#" * 55)
    print("           HEALTH SYSTEM PATIENT REGISTRY")
    print("#" * 55)

    if not patient_registry:
        print("\n [!] The registry is currently empty.\n")
        return

    for p_id, patient in patient_registry.items():
        patient.display_info()


def seed_sample_data() -> None:
    """Pre-populates sample data into the system for demonstration."""
    p1 = Patient("PAT-101", 32, "Female", "SL-FREETOWN-01")
    p2 = Patient("PAT-102", 54, "Male", "SL-BO-02")

    register_patient(p1)
    register_patient(p2)

    # Creating Medical Records with immutable vitals tuple (BP, HR, Temp)
    rec1 = MedicalRecord("REC-001", "Malaria Rapid Test Positive", "Artemether-Lumefantrine", ("120/80", 75, 38.4))
    rec2 = MedicalRecord("REC-002", "Hypertension Follow-up", "Amlodipine 5mg Daily", ("140/90", 82, 36.8))

    p1.add_medical_record(rec1)
    p1.add_medical_record(rec2)