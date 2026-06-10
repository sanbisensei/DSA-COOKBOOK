# School Management with Static Method
# Create a School class with a class variable total_students = 0. Each time a new student is created (via __init__), increment total_students. Add a @staticmethod called is_passing_grade(grade) that returns True if grade >= 50, else False. Also add a @staticmethod called school_motto() that returns a motto string.

# total_students is a class variable incremented in __init__

# is_passing_grade() takes only grade as argument — no self or cls

# Call School.is_passing_grade(45) and School.is_passing_grade(72) directly on the class

# Print total_students after creating 4 student objects


class School:
    total_students = 0  # class variable

    def __init__(self, name):
        self.name = name
        School.total_students += 1

    @staticmethod
    def is_passing_grade(grade):
        return grade >= 50

    @staticmethod
    def school_motto():
        return "Knowledge is Power"
    
s1 = School("A")
s2 = School("B")
s3 = School("C")
s4 = School("D")

print(School.total_students)

print(School.is_passing_grade(45))  # False
print(School.is_passing_grade(72))  # True
print(School.school_motto())        # Knowledge is Power