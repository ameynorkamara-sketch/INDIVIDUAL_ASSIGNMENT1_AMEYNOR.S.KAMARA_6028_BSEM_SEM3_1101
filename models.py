"""
models.py
Domain: Health Care System (Digital Public Goods compliant)
Contains class definitions for Patient and MedicalRecord.
"""


class MedicalRecord:
    """Class representing an individual patient visit/encounter."""

    def __init__(self, record_id: str, diagnosis: str, treatment: str, vitals: tuple):
        self.record_id = record_id
        self.diagnosis = diagnosis
        self.treatment = treatment
        
        self.vitals = vitals

    def display_record(self) -> None:
        """Instance Method: Formats and displays record details."""
        bp, hr, temp = self.vitals
        print(f"    ┌─ [Record ID: {self.record_id}]")
        print(f"    ├─ Diagnosis : {self.diagnosis}")
        print(f"    ├─ Treatment : {self.treatment}")
        print(f"    └─ Vitals    : BP {bp} mmHg | HR {hr} bpm | Temp {temp}°C")


class Patient:
    """Class representing an anonymized Patient in the healthcare system."""

    
    total_patients: int = 0

    def __init__(self, patient_id: str, age: int, gender: str, location_code: str):
        self.patient_id = patient_id
        self.age = age
        self.gender = gender
        self.location_code = location_code  
        self.medical_records = []  

        
        Patient.total_patients += 1

    def add_medical_record(self, record: MedicalRecord) -> None:
        """Instance Method: Interacts with a MedicalRecord object."""
        self.medical_records.append(record)
        print(f"[+] Record '{record.record_id}' added to Patient {self.patient_id}.")

    def display_info(self) -> None:
        """Instance Method: Displays detailed patient demographic & medical info."""
        print("=" * 55)
        print(f" PATIENT ID    : {self.patient_id}")
        print(f" Age           : {self.age}")
        print(f" Gender        : {self.gender}")
        print(f" Location Code : {self.location_code}")
        print(f" Total Encounters: {len(self.medical_records)}")
        print("-" * 55)

        if self.medical_records:
            print(" Medical Visit Records:")
            for record in self.medical_records:
                record.display_record()
                print()
        else:
            print("  No medical encounter records found for this patient.")
        print("=" * 55)

    @classmethod
    def get_total_patients(cls) -> int:
        """Class Method (@classmethod): Returns the total registered patient count."""
        return cls.total_patients

    @staticmethod
    def validate_patient_id(patient_id: str) -> bool:
        """Static Method (@staticmethod): Validates standard Patient ID formatting."""
        
        if patient_id.startswith("PAT-") and len(patient_id) == 7 and patient_id[4:].isdigit():
            return True
        return False