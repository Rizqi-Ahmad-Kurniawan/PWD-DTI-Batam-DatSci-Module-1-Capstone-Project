from tabulate import tabulate  
from Data_Class import AllData, DoctorData
from Data_DB import MainDB
# import pandas as pd

# DOCTOR Functions

# Display MainDB (READ)
def display_patientData():
    header = ["Patient ID", "Doctor ID", "Name", "Age", "Gender", "Diagnosis", "Lab Results", "Allergies"]

    if not MainDB:
        print("\nNo patients present !!!")
    else:
        print("\n ===== PATIENT HEALTH RECORDS ===== ")
        # Creating Iterable Object
        patients_data = [(index + 1, patient.patientID, patient.doctorID, patient.name, patient.age, patient.gender, patient.diagnosis, patient.labResults, patient.allergies) for index, patient in enumerate(MainDB)]
        print(tabulate(patients_data, headers=header, tablefmt="fancy_grid"))

# Add (Edit) new Patient data (class MedData) to MainDB (UPDATE)
def edit_patientData_doc():
    display_patientData()
    print("\n ===== EDIT PATIENT DATA (MED) ===== \n")
    targetPatientID = input("\nEnter Patient ID to be Edited (Med-Data):  ")
    for patientData in MainDB:
        if patientData.patientID.lower() == targetPatientID.lower():
            print(f"\nCurrent Medical Details of the Patient \"{patientData.patientID}\": ")
            print(" = = = = = = = = = = ")
            print(f"Doctor Notes: {patientData.docNotes}")
            print(f"Diagnosis: {patientData.diagnosis}")
            print(f"Prognosis: {patientData.prognosis}")
            print(f"Lab Results: {patientData.labResults}")
            print(f"Allergies: {patientData.allergies}")
            print(f"Medications: {patientData.medications}")
            
            # EDIT phase
            new_docNotes = input("\nUpdated Doctor Notes: (press enter to keep current): ")
            patientData.docNotes = new_docNotes if new_docNotes else patientData.docNotes
            
            new_diagnosis = input("Updated Diagnosis: (press enter to keep current): ")
            patientData.diagnosis = new_diagnosis if new_diagnosis else patientData.diagnosis
            
            new_prognosis = input("Updated Prognosis: (press enter to keep current): ")
            patientData.prognosis = new_prognosis if new_prognosis else patientData.prognosis
            
            new_labResults = input("Updated Lab Results [format: Avg BPM: x | BP(S/D): x/x | SPO2: x%]: (press enter to keep current): ")
            patientData.labResults = new_labResults if new_labResults else patientData.labResults
            
            new_allergies = input("Updated Allergies: (press enter to keep current): ")
            patientData.allergies = new_allergies if new_allergies else patientData.allergies
            
            new_medications = input("Updated Medications [format: drug_name (quantity_X/day)]: (press enter to keep current): ")
            patientData.medications = new_medications if new_medications else patientData.medications
            
            print(f"\nPatient \"{patientData.patientID}\" Medical Details Updated Successfully")
            return
    print("\nPatient not found !!!")
