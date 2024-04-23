# CLASSES
# Constructor = __init__

# Standalone class
class DoctorData():
    def __init__(self, doctorID, specialty, name, age, gender, phone, citizenID):
        self.doctorID = doctorID
        self.specialty = specialty
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.citizenID = citizenID

# Parent class
class BioData:
   def __init__(self, name, age, gender, phone, citizenID, occupation, sponsor):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.citizenID = citizenID
        self.occupation = occupation
        self.sponsor = sponsor

# Parent class
class MedData:
    def __init__(self, docNotes, diagnosis, prognosis, labResults, allergies, medications):
        self.docNotes = docNotes
        self.diagnosis = diagnosis
        self.prognosis = prognosis
        self.labResults = labResults
        self.allergies = allergies
        self.medications = medications
             
# Child Class (mainDB by "patientID" index)
class AllData(BioData, MedData):
    def __init__(self, patientID, doctorID, name, age, gender, phone, citizenID, occupation, sponsor, docNotes, diagnosis, prognosis, labResults, allergies, medications):
        self.patientID = patientID
        self.doctorID = doctorID
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.citizenID = citizenID
        self.occupation = occupation
        self.sponsor = sponsor
        self.docNotes = docNotes
        self.diagnosis = diagnosis
        self.prognosis = prognosis
        self.labResults = labResults
        self.allergies = allergies
        self.medications = medications
        
        # Invoking Parent Classes
        BioData.__init__(self, name, age, gender, phone, citizenID, occupation, sponsor)
        MedData.__init__(self, docNotes, diagnosis, prognosis, labResults, allergies, medications)
        
