class Hospital():
    docs = []
    patients = []

    def __init__(self):
        self.docs = []
        self.patients = []
        self.receipts = []

    def add_docs(self):
        name = input("enter the doctor name")
        age = input("enter the age doctor")
        major = input("enter the doctor major")
        hour_rate = input("enter the hour_rate")
        doc = Doctor(name, age, major, hour_rate)
        self.docs.append(Doctor)
    def add_patient(self):
        name = input("enter the patient name")
        age = input("enter the patient age")
        illness = input("enter the patient illness")
        self.patients.append(patient(name, age, illness))

class Doctor():
    name = ''
    age = 0
    major = ''
    hour_rate = ''

    def __init__(self, name, age, major, hour_rate):
        self.name = name
        self.age = age
        self.major = major
        self.hour_rate = hour_rate
        self.patients = []


class patient():
    name = ''
    age = 0
    illness = ''

    def __init__(self, name, age, illness):
        self.name = name
        self.age = age
        self.illness = illness
        self.docs = None
hospital = Hospital()
while True :
    print("pls select a choice\n")
    print(1-"add doc\n")
    print(2-"add patient")
    print(3-"")
    print("")
    choice = input()
    if choice == "1":
        hospital.add_docs()
    elif choice == "2":
        hospital.add_patient()

