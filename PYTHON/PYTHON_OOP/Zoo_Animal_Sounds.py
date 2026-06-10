# Zoo Animal Sounds
# Create a base class Animal with a method speak() that prints 'Some sound'. Create subclasses Dog, Cat, Parrot, and Snake, each overriding speak() with their own sound. Store all animals in a list and loop through them calling speak() on each.
# At least 4 animal subclasses
# Snake's speak() should print 'Ssssss'
# Loop through a list [Dog(), Cat(), Parrot(), Snake()] and call speak() on each

class Animal():
    def speak(self):
        print("Some Sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Parrot(Animal):
    def speak(self):
        print("kukki")

class Cat(Animal):
    def speak(self):
        print("Mew")

class Snake(Animal):
    def speak(self):
        print("Sssss")

ss = [Dog(), Parrot(), Cat(), Snake()]

for s in ss:
    s.speak()