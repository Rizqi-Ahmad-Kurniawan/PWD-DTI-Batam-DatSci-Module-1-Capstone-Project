from Data_DB import DoctorDB

# AUTHENTICATION & VALIDATION

# Index starts after the last idx in the existing database in "Data_DB.py"
patientID_counter = 6
doctorID_counter = 4
# User Credentials (password)
# Doctor uses Doctor IDs from DoctorDB
admID_1 = "Adm-1"
admID_2 = "Adm-2"


# AUTHENTICATION (Case-Sensitive Password for Multi-User)
def userAuth_admin():
    attempts = 0
    maxAttempts = 3
    
    while attempts <= maxAttempts:
        user_pass = input("Enter your Admin ID: ")
        if user_pass == admID_1:
            print("\nWelcome Admin 1 ;)")
            return user_pass
        elif user_pass == admID_2:
            print("\nWelcome Admin 2 ;)")
            return user_pass
        else:
            attempts += 1
            print(f"Incorrect Password. You have {maxAttempts - attempts} attempt(s) remaining !!!")
            if attempts == maxAttempts:
                print("Maximum attempts reached. The Program will now EXIT !!!")
                exit(0)

def userAuth_doctor():
    attempts = 0
    maxAttempts = 3
    while attempts <= maxAttempts:
        user_pass = input("Enter your Doctor ID: ")
        for doctorData in DoctorDB:
            if doctorData.doctorID == user_pass:
                print(f"\nWelcome Doctor \"{user_pass}\" ;)")
                attempts = 4
                return user_pass 
        if attempts <= maxAttempts:
            attempts += 1
            print(f"Incorrect Password. You have {maxAttempts - attempts} attempt(s) remaining !!!")
            if attempts == maxAttempts:
                print("Maximum attempts reached. The Program will now EXIT !!!")
                exit(0)

# ID GENERATOR
# patientID = input("\nEnter Patient ID [Pxxx]: ") -> Pat-1
# doctorID = input("Enter Doctor ID [Dxxx]: ") -> Doc-1

# For PatientID
def patientID_generator():
    global patientID_counter
    str1 = "Pat"
    str2 = str(patientID_counter)
    # Str Concat
    str3 = '-'.join([str1, str2])
    # Update to latest
    patientID_counter += 1
    return str3
    
# For DoctorID
def doctorID_generator():
    global doctorID_counter
    str1 = "Doc"
    str2 = str(doctorID_counter)
    # Str Concat
    str3 = '-'.join([str1, str2])
    # Update to latest
    doctorID_counter += 1
    return str3

# VALIDATION (string_len, data_type, specific)
# could Operate if the "Skip to Enter" feature is removed
def val_inp_specific(prompt, specific):
    user_input = input(prompt)
    while user_input not in specific:
        print("Invalid Input !!!")
        user_input = input(prompt)
    return user_input
def val_inp_dataType(prompt, dataType):
    while True:
        try:
            user_input = dataType(input(prompt))
            break
        except ValueError:
            print("Invalid Data Type !!!")
        return user_input
def val_inp_strlen(prompt, strlen):
    user_input = input(prompt)
    while len(user_input) < strlen:
        print(f"Input must be {strlen} characters long !!!")
        user_input = input(prompt)
    return user_input
