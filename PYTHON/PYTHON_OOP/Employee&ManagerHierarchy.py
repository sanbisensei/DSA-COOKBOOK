# Employee & Manager Hierarchy
# Create a parent class Employee with name, employee_id, and salary. Add a method get_info(). Then create a child class Manager that adds a department attribute and overrides get_info() to also show the department. Create a third class Intern that adds duration_months and overrides get_info().
# Manager and Intern must call super().__init__() properly
# Both child classes override get_info() and extend the parent's version using super()
# Create 2 Employee, 2 Manager, and 1 Intern objects


class Employee:
    def __init__(self,name,employee_id,salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    def get_info(self):
        return f"Name: {self.name}, ID: {self.employee_id}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self,name,employee_id,salary,department):
        super().__init__(name,employee_id,salary)
        self.department = department

    def get_info(self):
        return f"{super().get_info()}, Department: {self.department}"

class Intern(Employee):
    def __init__(self,name,employee_id,salary,duration_months):
        super().__init__(name,employee_id,salary)
        self.duration_months = duration_months

    def get_info(self):
        return f"{super().get_info()}, Duration: {self.duration_months}"



one = Intern("Hammer",397,400000,"5months")
print(one.get_info())