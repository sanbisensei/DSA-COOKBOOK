# Student Grade Tracker
# Create a class Student with a class variable school = 'Tech Academy' and instance variables name and grades (a dictionary mapping subject → grade). Add methods: add_grade(subject, grade), get_average(), and display_report() that prints all subjects and grades. Create 3 students and add grades to each.
# grades is a dict: {'Math': 85, 'Science': 90}
# add_grade() updates the dict
# get_average() uses a for loop to sum values and divides by count
# display_report() loops over the dict and prints each subject + grade




class Student:
    school = "Tech Academy"

    def __init__(self, name):
        self.name = name
        self.grades = {} 

    def add_grade(self,subject,grade):
        self.grades[subject] = grade
    
    def get_average(self):
        total =0
        count =0

        for grade in self.grades.values():
            total += grade
            count +=1

        if count == 0:
            return 0
        
        else:
            return total/count
    
    def display_report(self):
        print(f"\nStudent: {self.name}" )
        print(f"School: {Student.school}")
        
        for subject,grade in self.grades.items():
            print(f"{subject}: {grade}")

        
        print(f"Average: {self.get_average()}")


s1 = Student("Alice")
s2 = Student("Bob")
s3 = Student("Charlie")

s1.add_grade("Math", 85)
s1.add_grade("Science", 90)

s2.add_grade("Math", 70)
s2.add_grade("Science", 75)

s3.add_grade("Math", 95)
s3.add_grade("Science", 88)

s1.display_report()
s2.display_report()
s3.display_report()