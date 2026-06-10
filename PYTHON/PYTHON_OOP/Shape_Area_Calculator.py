# Shape Area Calculator (Abstract)
# Using from abc import ABC, abstractmethod, create an abstract class Shape with two abstract methods: area() and describe(). Implement three concrete classes: Triangle (base, height), Rectangle (length, width), and Circle (radius). Store all shapes in a list and print each shape's description and area.
# Shape must be abstract — trying to instantiate it directly should raise an error
# Triangle area = 0.5 * base * height
# All three classes fully implement both abstract methods
# describe() should print something like 'Triangle with base 5 and height 3'


from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def describe(self):
        pass

class Triangle(shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5 

    def describe(self):
        return "this is a Triangle"


class Rectangle(shape):
    def __init__(self,length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def describe(self):
        return "this is a Rectangle"




class Circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def describe(self):
        return "this is a Circle"
    

things = [Triangle(3,4), Rectangle(3,4), Circle(3)]

for thing in things:
    print(f"{thing.describe()} area of {thing.area()}")