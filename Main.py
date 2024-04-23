from User_Admin import *
from User_Doctor import * 
from Auth_Val import *

# check the condition if the script runs directly as the main program
# Main User Interface (menus)

if __name__ == "__main__":
    
    def login_page():
        print('''
            \n\t\tPATIENT RECORDS SYSTEM 
            "May Your Health be Everlasting"
            
            Confirm your IDENTITY:
            Press
            1 for Admin-access
            2 for Doctor-access
            3 to QUIT Program
            ''')
        menuChoice = int(input("Your Input: "))
        return menuChoice
    
    def admin_page(id):
        print(f'''
            \n\t\tPATIENT RECORDS SYSTEM 
            "May Your Health be Everlasting"
            
            Acessing as ADMIN \"{id}\":
            Press
            1 to Display patient data
            2 to Display doctor data
            3 to Add patient data
            4 to Add doctor data
            5 to Edit patient data (BioData)
            6 to Edit doctor data
            7 to Delete patient data
            8 to Delete doctor data
            9 to EXIT to Login page
            10 to QUIT Program
            ''')
        menuChoice = int(input("Your Input: "))
        return menuChoice
    
    def doctor_page(id):
        print(f'''
            \n\t\tPATIENT RECORDS SYSTEM 
            "May Your Health be Everlasting"
            
            Acessing as DOCTOR \"{id}\":
            Press
            1 to Display patient data
            2 to Edit patient data (MedData)
            3 to EXIT to Login page
            4 to QUIT Program
            ''')
        menuChoice = int(input("Your Input: "))
        return menuChoice
    
    # MAIN PROGRAM
    while True:
        try:
            menuChoice = login_page()
            if menuChoice == 1:
                loginCredential = userAuth_admin()
                while True:
                    try:
                        subMenuChoice_1 = admin_page(loginCredential)
                        if subMenuChoice_1 == 1:
                            display_patientData()
                        elif subMenuChoice_1 == 2:
                            display_doctorData()
                        elif subMenuChoice_1 == 3:
                            add_patientData()
                        elif subMenuChoice_1 == 4:
                            add_doctorData()
                        elif subMenuChoice_1 == 5:
                            # BioData
                            edit_patientData_adm()
                        elif subMenuChoice_1 == 6:
                            edit_doctorData()
                        elif subMenuChoice_1 == 7:
                            del_patientData()
                        elif subMenuChoice_1 == 8:
                            del_doctorData()
                        elif subMenuChoice_1 == 9:
                            break
                        elif subMenuChoice_1 == 10:
                            print(" THANKS FOR LOGGING IN :)))")
                            exit(0)
                        else:
                            print("Please enter the correct number !!!")
                    except Exception as e:
                        print("The error is: ", e)
            elif menuChoice == 2:
                loginCredential = userAuth_doctor()
                while True:
                    try:
                        subMenuChoice_2 = doctor_page(loginCredential)
                        if subMenuChoice_2 == 1:
                            display_patientData()
                        elif subMenuChoice_2 == 2:
                            # MedData
                            edit_patientData_doc()
                        elif subMenuChoice_2 == 3:
                            break
                        elif subMenuChoice_2 == 4:
                            print(" THANKS FOR LOGGING IN :)))")
                            exit(0)
                        else:
                            print("Please enter the correct number !!!")
                    except Exception as e:
                        print("The error is: ", e)
            elif menuChoice == 3:
                print(" THANKS FOR LOGGING IN :)))")
                exit(0)
            else:
                print("Please enter the correct number !!!")
        except Exception as e:
            print("The error is: ", e)
 