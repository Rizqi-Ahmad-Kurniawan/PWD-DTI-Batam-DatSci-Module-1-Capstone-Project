# INSTANCE/OBJECT Creation (copy of an class)
# Contains Child Class "AllData" (var count: 15) & "DoctorData" (var count: 7)
# "AllData" atrributes are inherited from Parent Class: BioData, MedData

from Data_Class import AllData, DoctorData


MainDB = [
    AllData('Pat-1', 'Doc-1', 'Borzul Alfonso', 45, 'M', '081234673422', '3728394720133477', 'Carpenter', 'Gov-Insurance', 'All vitals remain stable, sore eyes', 'Mild head trauma', 'The trauma will lessen in circa 3 days, expect sleep deprivation', 'Avg BPM: 112 | BP(S/D): 140/70 | SPO2: 88%', 'Peanuts', 'Diaprosol (2X/day) + Propanol (1X/day)'),
    AllData('Pat-2', 'Doc-2', 'Rielbia Basson', 32, 'F', '081245103827', '9544812278300093', 'Pet Shop Owner', 'Self-Insurance', 'Heart rate is volatile, runny eyes', 'Trimester Pregnancy Checkup', 'Sleep deprivation and loss of agility can be expected', 'Avg BPM: 140 | BP(S/D): 150/90 | SPO2: 92%', 'None', 'Comeprazol (3X/day) + Viacabol (2X/day)'),
    AllData('Pat-3', 'Doc-3', 'Besikta Almahdi', 65, 'M', '081288883110', '4099711123498277', 'Electrician', 'None', 'SP02 is low, with difficulty on breathing', 'Asphyxia', 'The lungs will get better in circa 2 weeks', 'Avg BPM: 132 | BP(S/D): 120/100 | SPO2: 68%', 'Jelly', 'Brofolix (3X/day)'),
    AllData('Pat-4', 'Doc-1', 'Ali Cisavva', 43, 'M', '081241220654', '8322999455673325', 'Boxer', 'Self-Insurance', 'Blunt impact on left prefrontal lobe with haemorrhage', 'Heavy head trauma', 'The headache will worsen in circa 10 days', 'Avg BPM: 137 | BP(S/D): 125/85 | SPO2: 95%', 'Orange', 'Pneumasol (1X/day) + Aptinin (3X/day)'),
    AllData('Pat-5', 'Doc-2', 'Matilda Al-Furqan', 28, 'F', '081288883344', '7882210944428784', 'Housewife', 'None', 'All vitals remain stable, dry mouth', 'Baby-induced loss of appetite', 'The loss of appetite will prevail for circa 5 days, expect dehydration and mild headache', 'Avg BPM: 117 | BP(S/D): 130/75 | SPO2: 98%', 'None', 'Omeprazol (3X/day) + Nutriabetic (1X/day)')
]

# DoctorsDB
DoctorDB = [
    DoctorData('Doc-1', 'Neurologist', 'Rizqi Ahmad', 23, 'M', '081256738294', '1356946739662311'),
    DoctorData('Doc-2', 'Obstetrician & Gynecologist', 'Barbara Fadhillah', 37, 'F', '081292334990', '0923772189367442'),
    DoctorData('Doc-3', 'Internal Diseases', 'Furqan Alexsov', 32, 'M', '081237843300', '9211632123987220')
]


# ============================
# OPTIONAL CODE SNIPPETS

# patientID: Any, doctorID: Any, name: Any, age: Any, gender: Any, phone: Any, citizenID: Any, occupation: Any, sponsor: Any, docNotes: Any, diagnosis: Any, prognosis: Any, labResults: Any, allergies: Any, medications: Any) -> None