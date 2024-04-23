from tabulate import tabulate  
from User_Doctor import * 
from Auth_Val import * 
from Data_Class import AllData, DoctorData
from Data_DB import MainDB, DoctorDB
#import pandas as pd 

# ADMIN Functions

# Display DoctorDB (READ)
def display_doctorData():
    header = ["Doctor ID", "Speciality", "Name", "Age", "Gender", "Phone", "Citizen ID"]

    if not MainDB:
        print("\nNo patients present !!!")
    else:
        print("\n ===== DOCTOR RECORDS ===== ")
        # Creating Iterable Object
        doctors_data = [(index + 1, doctor.doctorID, doctor.specialty, doctor.name, doctor.age, doctor.gender, doctor.phone, doctor.citizenID) for index, doctor in enumerate(DoctorDB)]
        print(tabulate(doctors_data, headers=header, tablefmt="fancy_grid"))

# Add new Patient data (class BioData) to MainDB (CREATE)
def add_patientData():
    print("\n ===== ADD PATIENT DATA ===== \n")
    # Auto-Generated ID
    patientID = patientID_generator()
    while True:
        flag = False
        doctorID = input("\nEnter Doctor ID for PIC [format: Doc-x]:): ")
        # Iterating to each
        for doctorData in DoctorDB:
            if doctorData.doctorID == doctorID:
                flag = True
                break
        if flag == True:
            break
        else:
            print(f"Doctor ID \"{doctorID}\" not found !!!") 
    name = input("Enter Name: ")
    while True:
        try:
            age = int(input("Enter Age: "))
            break
        except ValueError:
            print("Input must be an Integer/Number")
    while True:
        gender = input("Enter Gender: ").upper()
        if gender == "F" or gender == "M":
            break
        else: 
            print("Input must be 'M' or 'F' !!!")
    while True:
        phone = input("Enter Phone Number: ")
        if len(phone) == 12 and phone.isdigit() == True:
            break
        else: 
            print("Input must be 12 characters long and numeric only !!!")
    while True:
        citizenID = input("Enter Citizen ID: ")
        if len(citizenID)== 16 and citizenID.isdigit() == True:
            break
        else: 
            print("Input must be 16 characters long and numeric only !!!")
    occupation = input("Enter Occupation: ")
    sponsor = input("Enter Sponsor: ")
    docNotes = " None "
    diagnosis = " None "
    prognosis = " None "
    labResults = " None "
    allergies = " None "
    medications = " None "
    # Append
    MainDB.append(AllData(patientID, doctorID, name, age, gender, phone, citizenID, occupation, sponsor, docNotes, diagnosis, prognosis, labResults, allergies, medications))
    print(f"\nPatient \"{patientID}\" data added succesfully !!!")

# Add new Doctor data to MainDB (CREATE)
def add_doctorData():
    print("\n ===== ADD DOCTOR DATA ===== \n")
    # Auto-Generated ID
    doctorID = doctorID_generator()
    specialty = input("Enter Doctor Specialisation: ")
    name = input("Enter Name: ")
    while True:
        try:
            age = int(input("Enter Age: "))
            break
        except ValueError:
            print("Input must be an Integer/Number")
    while True:
        gender = input("Enter Gender: ").upper()
        if gender == "F" or gender == "M":
            break
        else: 
            print("Input must be 'M' or 'F' !!!")
    while True:
        phone = input("Enter Phone Number: ")
        if len(phone) == 12 and phone.isdigit() == True:
            break
        else: 
            print("Input must be 12 characters long and numeric only !!!")
    while True:
        citizenID = input("Enter Citizen ID: ")
        if len(citizenID)== 16 and citizenID.isdigit() == True:
            break
        else: 
            print("Input must be 16 characters long and numeric only !!!")
    # Append
    DoctorDB.append(DoctorData(doctorID, specialty, name, age, gender, phone, citizenID))
    print(f"\nDoctor \"{doctorID}\" data added succesfully !!!")

# Add (Edit) new Patient data (class MedData) to MainDB (UPDATE)
def edit_patientData_adm():
    display_patientData()
    print("\n ===== EDIT PATIENT DATA (BIO) ===== \n")
    targetPatientID = input("\nEnter Patient ID to be Edited (Bio-Data):  ")
    for patientData in MainDB:
        if patientData.patientID.lower() == targetPatientID.lower():
            print(f"\nCurrent Bio Details of Patient \"{patientData.patientID}\": ")
            print("= = = = = = = = = = ")
            print(f"Patient ID: {patientData.patientID}")
            print(f"Doctor ID: {patientData.doctorID}")
            print(f"Name: {patientData.name}")
            print(f"Age: {patientData.age}")
            print(f"Gender: {patientData.gender}")
            print(f"Phone: {patientData.phone}")
            print(f"Citizen ID: {patientData.citizenID}")
            print(f"Occupation: {patientData.occupation}")
            print(f"Sponsor: {patientData.sponsor}")
            
            # EDIT phase
            while True:
                flag = False
                new_doctorID = input("\nUpdated Doctor ID (reassign Doctor to new Patient): ")
                # Iterating to each
                for doctorData in DoctorDB:
                    if doctorData.doctorID == new_doctorID:
                        patientData.doctorID = new_doctorID
                        flag = True
                        break
                if flag == True:
                    break
                else:
                    print(f"Doctor ID \"{new_doctorID}\" not found !!!")    
        
            new_name = input("Updated Patient Name: (press enter to keep current): ")
            patientData.name = new_name if new_name else patientData.name
            
            while True:
                try:
                    new_age = int(input("Updated Patient Age: "))
                    patientData.age = new_age
                    break
                except ValueError:
                    print("Input must be an Integer/Number")
            
            while True:
                new_gender = input("Updated Patient Gender: ").upper()
                if new_gender == "F" or new_gender == "M":
                    patientData.gender = new_gender
                    break
                else: 
                    print("Input must be 'M' or 'F' !!!")
            
            while True:
                new_phone = input("Updated Phone Number: ")
                if len(new_phone) == 12 and new_phone.isdigit() == True:
                    patientData.phone = new_phone
                    break
                else: 
                    print("Input must be 12 characters long and numeric only !!!")
            
            while True:
                new_citizenID = input("Updated Citizen ID: ")
                if len(new_citizenID)== 16 and new_citizenID.isdigit() == True:
                    patientData.citizenID = new_citizenID
                    break
                else: 
                    print("Input must be 16 characters long and numeric only !!!")
            
            new_occupation = input("Updated Occupation: (press enter to keep current): ")
            patientData.occupation = new_occupation if new_occupation else patientData.occupation
            
            new_sponsor = input("Updated Sponsor: (press enter to keep current): ")
            patientData.sponsor = new_sponsor if new_sponsor else patientData.sponsor
            
            print(f"\nPatient \"{patientData.patientID}\" Bio Details Updated Successfully")
            return
    print(f"\nPatient \"{targetPatientID}\" not found !!!")

# Add (Edit) new Doctor data to DoctorDB (UPDATE)
def edit_doctorData():
    display_doctorData()
    print("\n ===== EDIT DOCTOR DATA ===== \n")
    targetDoctorID = input("\nEnter Doctor ID to be Edited:  ")
    for doctorData in DoctorDB:
        if doctorData.doctorID.lower() == targetDoctorID.lower():
            print(f"\nCurrent Details of Doctor \"{doctorData.doctorID}\": ")
            print("= = = = = = = = = = ")
            print(f"Doctor ID: {doctorData.doctorID}")
            print(f"Specialty: {doctorData.specialty}")
            print(f"Name: {doctorData.name}")
            print(f"Age: {doctorData.age}")
            print(f"Gender: {doctorData.gender}")
            print(f"Phone: {doctorData.phone}")
            print(f"Citizen ID: {doctorData.citizenID}")
            
            # EDIT phase  
            new_specialty = input("\nUpdated Doctor Specialty: (press enter to keep current): ")
            doctorData.specialty = new_specialty if new_specialty else doctorData.specialty
            
            new_name = input("Updated Doctor Name: (press enter to keep current): ")
            doctorData.name = new_name if new_name else doctorData.name
            
            while True:
                try:
                    new_age = int(input("Updated Doctor Age: "))
                    doctorData.age = new_age
                    break
                except ValueError:
                    print("Input must be an Integer/Number")
            
            while True:
                new_gender = input("Updated Doctor Gender: ").upper()
                if new_gender == "F" or new_gender == "M":
                    doctorData.gender = new_gender
                    break
                else: 
                    print("Input must be 'M' or 'F' !!!")
            
            while True:
                new_phone = input("Updated Phone Number: ")
                if len(new_phone) == 12 and new_phone.isdigit() == True:
                    doctorData.phone = new_phone
                    break
                else: 
                    print("Input must be 12 characters long and numeric only !!!")
            
            while True:
                new_citizenID = input("Updated Citizen ID: ")
                if len(new_citizenID) == 16 and new_citizenID.isdigit() == True:
                    doctorData.citizenID = new_citizenID
                    break
                else: 
                    print("Input must be 16 characters long and numeric only!!!")
            
            print(f"\nDoctor \"{doctorData.doctorID}\" Details Updated Successfully")
            return
    print(f"\nDoctor \"{targetDoctorID}\" not found !!!")

# Delete (by Patient ID) existing Patient Data (class AllData) from MainDB (DELETE)
def del_patientData():
    display_patientData()
    print("\n ===== DELETE PATIENT DATA ===== \n")
    user_input = input("\nEnter Patient ID to be deleted: ")
    for patientData in MainDB:
        if patientData.patientID.lower() == user_input.lower():
            MainDB.remove(patientData)
            print(f"\nPatient \"{patientData.patientID}\" record deleted successfully !!!")
            return
    print(f"\nPatient \"{user_input}\" record not found !!!")

# Delete (by Doctor ID) existing Doctor Data (class DoctorData) from DoctorDB (DELETE)
def del_doctorData():
    flag_docDB = False
    flag_patDB = False
    
    display_doctorData()
    print("\n ===== DELETE DOCTOR DATA ===== \n")
    user_input = input("\nEnter Doctor ID to be deleted: ")
    # Validation of Existance in DoctorDB
    for doctorData in DoctorDB:
        if doctorData.doctorID.lower() == user_input.lower():
            flag_docDB = True        
    # Validation if Doctor cannot be DELETED due to it being a PIC
    for patientData in MainDB:
        if patientData.doctorID.lower() == user_input.lower():
            flag_patDB = True
    
    # Actions
    if flag_docDB == False:
        if flag_patDB == False or flag_patDB == True:
            print(f"Doctor \"{user_input}\" record not found !!!")
            return 
    elif flag_docDB == True and flag_patDB == False:
        # Deletion process (after var "user_input" validation)
        for doctorData in DoctorDB:
            if doctorData.doctorID.lower() == user_input.lower():
                DoctorDB.remove(doctorData)
                print(f"Doctor \"{doctorData.doctorID}\" record deleted successfully !!!")
        return 
    else: # flag_docDB == True and flag_patDB == True
        print(f"\nDoctor \"{user_input}\" record CANNOT be deleted due to ONGOING assignment as PIC for Patient(s) !!!")
        return
                

# ============================
# OPTIONAL CODE SNIPPETS

# header = ["Patient ID", "Doctor ID", "Name", "Age", "Gender", "Phone", "Citizen ID", "Occupation", "Sponsor", "Doc_Notes", "Diagnosis", "Prognosis", "Lab Results", "Allergies", "Medications"]

# patients_data = [(index + 1, patient.patientID, patient.doctorID, patient.name, patient.age, patient.gender, patient.phone, patient.citizenID, patient.occupation, patient.sponsor, patient.docNotes, patient.diagnosis, patient.prognosis, patient.labResults, patient.allergies, patient.medications) for index, patient in enumerate(MainDB)]

# Pandas
    # pdDataFrame = pd.DataFrame(patients_data)
    # result = pdDataFrame.transpose();
    # transposed = list(map(list, zip(*patients_data)))
