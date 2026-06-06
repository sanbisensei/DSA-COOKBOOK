# Problem : Create a Car class with attribute like brand and model. Then create an instance of the class.

# Problem : Add a method to the Car Class that displays the full name of the car(brand and model)

# Problem : Create an ElectricCar class that inherits from the Car class and has an additional Attribute battery_size

# Problem : Modify the Car class to encapsulate the brand attribute,making it private and provide a getter method

# Problem : Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

# Problem : Add a class variable to Car that keeps track of number of cars created.

# Problem : Add a static method to the Car class that returns a general description of a car.

# Problem : use a property decorator in the Car class to make the model attribute read-only.

# Problem : Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar

class Car:


    total_car = 0


    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model

        Car.total_car += 1


    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Disel"
    
    @property
    def model(self):
        return self.__model

    @staticmethod
    def general_description():
        return "Cars are means of transport"



class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        # self.brand = brand
        # self.model = model
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"



my_car = Car("Toyota","Supra")
# my_car.model = "Bully"
# print(my_car.model) 
# print(my_car.brand)
# print(my_car.full_name())
# my_new_car = Car("Tata","Safari")
# print(my_new_car.brand)


my_tesla = ElectricCar("Tesla","Model S","85KW")

print(isinstance(my_tesla,Car))
# print(my_tesla.brand())
# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())


# my_lambo = Car("Lamborgini","Galardo")
# my_Mustange = Car("Mustang","GT")
# my_Ferrari = Car("Ferrari","Lcrc102")
# print(my_lambo.fuel_type())

# print(Car.total_car)

# print(Car.general_description())