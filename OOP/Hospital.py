class Patient(object):
    patient_id = 0
    def __init__(self, name, allergies):
        Patient.patient_id += 1
        self.name = name 
        self.allergies = allergies 
        self.bed_num = None 
    
class Hospital(object):
    bed_num = 0
    def __init__(self, name, capacity):
        self.name = name 
        self.capacity = capacity 
        self.patients = []

    def admit(self, patient):
        if (len(self.patients) < self.capacity):
            self.patients.append(patient)
            Hospital.bed_num += 1
            patient.bed_num = Hospital.bed_num
            return "Admission confirmed"
        return "Hospital is Full. Sorry"

    def discharge(self, patient):
        patient.bed_num = None
        self.patients.remove(patient)

p1 = Patient("Todd", "Gluten")
p2 = Patient("Brittany", "Gluten, Soy, Dairy, Sesame, Mushroom, Almond")
p3 = Patient("Connie", "Sulfa")

h1 = Hospital("Mercy General",3)
h1.admit(p1)
h1.admit(p2)
h1.admit(p3)
print h1.admit(p1)

print h1.patients

h1.discharge(p1)

print h1.patients
print p1.bed_num
print p2.bed_num
        

