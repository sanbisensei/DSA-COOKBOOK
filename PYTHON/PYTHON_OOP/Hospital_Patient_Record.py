# Hospital Patient Records
# Create a base class Person with private __name and __age with getters/setters. Create a child class Patient that adds a medical_history list (list of strings) and methods add_record(condition) and show_history(). Create 3 patients, add multiple medical records to each, then store all patients in a list and loop through showing each patient's full info and history.

# Private attributes with proper getters in Person
# Patient inherits from Person using super()
# medical_history is a list that grows with add_record()
# show_history() loops through the list and prints each item
# A final loop: for patient in all_patients: patient.show_history()




class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # getters
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # setters
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")


class Patient(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.medical_history = []

    def add_record(self, condition):
        self.medical_history.append(condition)

    def show_history(self):
        print(f"\nPatient: {self.get_name()}, Age: {self.get_age()}")
        print("Medical History:")
        for record in self.medical_history:
            print("-", record)

p1 = Patient("Ali", 25)
p2 = Patient("Sara", 30)
p3 = Patient("Rahim", 40)


p1.add_record("Fever")
p1.add_record("Cold")

p2.add_record("Diabetes")
p2.add_record("Blood Pressure")

p3.add_record("Asthma")
p3.add_record("Allergy")


all_patients = [p1, p2, p3]
for patient in all_patients:
    patient.show_history()