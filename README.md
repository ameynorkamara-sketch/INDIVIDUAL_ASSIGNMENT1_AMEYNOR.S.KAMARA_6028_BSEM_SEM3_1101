# Patient Record System (Open Health Infrastructure)

A modular Python program developed using Object-Oriented Programming (OOP) concepts for managing health encounters, aligned with **Digital Public Goods (DPG)** standards.

## Project Details
- **Module**: Object-Oriented Programming 1 (PROG211)
- **Institution**: Limkokwing University of Creative Technology, Sierra Leone
- **Examiner**: Amandu Kamara
- **Domain**: Health Care System

---

## Digital Public Goods (DPG) Standards Compliance
1. **Open Source**: Released under the MIT License for open adaptation and community contribution.
2. **Privacy-Respecting**: Zero Personally Identifiable Information (PII) is stored. Patient records use anonymized IDs (`PAT-XXX`) and regional location codes rather than full names or home addresses.
3. **Modular & Reusable**: Separated into independent modules (`models.py`, `registry.py`, `main.py`) allowing reusability across health programs or vaccination trackers.
4. **Inclusive & Lightweight**: Runs efficiently on low-tier systems using the standard Python environment.

---

## Summary of OOP & Data Structure Concepts
- **Task 1 (Classes & Objects)**:
  - `Patient`: Represents patient entries with demographic data and history lists.
  - `MedicalRecord`: Holds individual medical encounter records linked to a patient.
- **Task 2 (Data Structures)**:
  - **Dictionary (`patient_registry`)**: Maps unique patient IDs (`PAT-XXX`) to `Patient` objects for rapid key-value lookup.
  - **Tuple (`vitals`)**: Encapsulates immutable clinical metrics `(Blood Pressure, Heart Rate, Temperature)`.
- **Task 3 (Methods & Encapsulation)**:
  - **Instance Methods**: `add_medical_record()`, `display_info()`, `display_record()`.
  - **Class Method**: `@classmethod get_total_patients()` to query total created patient instances.
  - **Static Method**: `@staticmethod validate_patient_id()` to verify ID formatting rules.

---

## How to Run in VS Code

1. Open **VS Code**.
2. Select **File -> Open Folder...** and select the `patient_record_system` folder.
3. Open the integrated terminal (`Ctrl + ~` or `Cmd + ~`).
4. Run the application:
   ```bash
   python main.py