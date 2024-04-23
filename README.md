# ✨✨✨ Capstone_Project_1_Purwadhika ✨✨✨

# Patient Record System


## Presentation (visual overview)
Canva Link: https://www.canva.com/design/DAGDP-iVE18/F4EyiVI7CxlgxhAd_ddBCQ/view?utm_content=DAGDP-iVE18&utm_campaign=designshare&utm_medium=link&utm_source=editor  


## Overview
- Capstone project for learning module 1 of Purwadhika DTI Data Science Program. 
- The project is a simple Command-Line application written in Python. 
- It allows users the option to Create (add), Read (display), Update (edit), and Delete Patient and Doctor records present in Hospitals.
- The Users of the CLI-App are "Administrators" and "Doctors", each with its own set of User Interface features.
- The theme/case of the CLI-App is to create a Medical Data Management System (with user authentication) where "Admins" can manage Doctor and Patient Data and "Doctors" can view and edit (input/renew) Patient data as needed.


## Features (main | explicit)
> as ADMIN ->
- Display patient data
- Display doctor data
- Add patient data
- Add doctor data
- Edit patient data (BioData)
- Edit doctor data
- Delete patient data
- Delete doctor data
> as DOCTOR ->
- Display patient data
- Edit patient data (MedData)


## Features (additional | implicit)
- OOP implementation (modular database)
- Multi-User Interface (tailored UI)
- Auto-Generated PatientID and DoctorID
- User Authentication with password attempt limit
- Input Validation (based on datatype and Patient or DoctorID)


## Usage
1. Clone repository to your local machine: https://github.com/Rizqi-Ahmad-Kurniawan/PWD-DTI-Batam-DatSci-Module-1-Capstone-Project.git 
2. Ensure that you have Python installed
3. Install the required dependencies by running `pip install -r requirements.txt`
4. Run the `main.py` file using Python from an IDE (integrated development environment)
5. Follow the on-screen instructions to navigate through the application and manage Doctor and Patient Data


## Dependencies
- Python 3.x
- Tabulate: for displaying Data in formatted tables


## Setup environment
```
pip install tabulate
```
