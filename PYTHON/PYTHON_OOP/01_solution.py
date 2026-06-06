# Problem : Create a Car class with attribute like brand and model. Then create an instance of the class.

# Problem : Add a method to the Car Class that displays the full name of the car(brand and model)

# Problem : Create an ElectricCar class that inherits from the Car class and has an additional Attribute battery_size

# Problem : Modify the Car class to encapsulate the brand attribute,making it private and provide a getter method

#

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.model}"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        # self.brand = brand
        # self.model = model
        super().__init__(brand,model)
        self.battery_size = battery_size

# my_car = Car("Toyota","Supra")
# print(my_car.brand)
# print(my_car.full_name())
# my_new_car = Car("Tata","Safari")
# print(my_new_car.brand)


my_tesla = ElectricCar("Tesla","Model S","85KW")
print(my_tesla.brand())
print(my_tesla.get_brand())