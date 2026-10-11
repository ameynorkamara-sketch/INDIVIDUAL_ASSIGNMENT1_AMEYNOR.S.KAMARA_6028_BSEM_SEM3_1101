"""
main.py
Main Execution File / Interactive Command-Line Interface.
Run this file directly inside VS Code terminal.
"""

import sys
from models import Patient, MedicalRecord
from registry import (
    patient_registry,
    register_patient,
    find_patient,
    display_all_patients,
    seed_sample_data,
)


def print_menu():
    print("\n" + "=" * 45)
    print("   PATIENT RECORD SYSTEM (DPG COMPLIANT)")
    print("=" * 45)
    print(" 1. Register New Patient")
    print(" 2. Add Medical Encounter Record to Patient")
    print(" 3. View Specific Patient Details")
    print(" 4. View All Registered Patients")
    print(" 5. View Total Patient Count (Class Method)")
    print(" 6. Exit Program")
    print("=" * 45)


def handle_add_patient():
    print("\n--- Register New Patient ---")
    p_id = input("Enter Patient ID (Format PAT-XXX, e.g., PAT-103): ").strip().upper()
    
    if not Patient.validate_patient_id(p_id):
        print("[!] Validation Failed: Patient ID must start with 'PAT-' followed by 3 numbers.")
        return

    try:
        age = int(input("Enter Age: ").strip())
    except ValueError:
        print("[!] Invalid age entered.")
        return

    gender = input("Enter Gender (Female/Male/Other): ").strip().capitalize()
    location = input("Enter Location Region Code (e.g., SL-KENEMA-03): ").strip().upper()

    new_patient = Patient(p_id, age, gender, location)
    register_patient(new_patient)


def handle_add_medical_record():
    print("\n--- Add Medical Record ---")
    p_id = input("Enter Patient ID to attach record (e.g., PAT-101): ").strip().upper()
    patient = find_patient(p_id)

    if not patient:
        print(f"[!] Patient with ID '{p_id}' not found.")
        return

    rec_id = input("Enter Medical Record ID (e.g., REC-003): ").strip().upper()
    diagnosis = input("Enter Diagnosis: ").strip()
    treatment = input("Enter Prescribed Treatment: ").strip()

    print("\nEnter Medical Vitals:")
    bp = input(" Blood Pressure (e.g., 120/80): ").strip()
    try:
        hr = int(input(" Heart Rate (bpm): ").strip())
        temp = float(input(" Temperature (°C): ").strip())
    except ValueError:
        print("[!] Invalid numeric inputs for Heart Rate or Temperature.")

        
 # Tuple data structure
    vitals_tuple = (bp, hr, temp) 
    record = MedicalRecord(rec_id, diagnosis, treatment, vitals_tuple)
    patient.add_medical_record(record)


def handle_view_patient():
    print("\n--- Search Patient ---")
    p_id = input("Enter Patient ID (e.g., PAT-101): ").strip().upper()
    patient = find_patient(p_id)

    if patient:
        patient.display_info()
    else:
        print(f"[!] Patient '{p_id}' not found.")


def main():
    print("Initializing Patient Record System...")
    seed_sample_data()  # Seed initial test records

    while True:
        print_menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            handle_add_patient()
        elif choice == "2":
            handle_add_medical_record()
        elif choice == "3":
            handle_view_patient()
        elif choice == "4":
            display_all_patients()
        elif choice == "5":
            total = Patient.get_total_patients()
            print(f"\n[i] Class Method Executed: Total Patients in System = {total}")
        elif choice == "6":
            print("\nExiting Patient Record System. Goodbye!")
            sys.exit(0)
        else:
            print("\n[!] Invalid selection. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()