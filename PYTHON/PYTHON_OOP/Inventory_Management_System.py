# This is your boss-level challenge. Build an Inventory system. Create an abstract class Item with abstract method get_details(). Create two concrete classes: Electronics (name, price, warranty_years) and Clothing (name, price, size). Create an Inventory class with a private __items list. Add methods: add_item(item), remove_item(name), search_by_type(item_type), total_value(), and display_all(). Use a class variable to track total_items_ever_added.

# Item is abstract (ABC), get_details() is abstract
# Electronics and Clothing both implement get_details()
# Inventory uses __items (private list) with getter
# search_by_type() takes 'Electronics' or 'Clothing' and returns filtered list using isinstance()
# total_value() sums all item prices
# Class variable tracks total items ever added (not current count)


from abc import ABC, abstractmethod


# ----------------- ABSTRACT BASE CLASS -----------------
class Item(ABC):
    @abstractmethod
    def get_details(self):
        pass


# ----------------- CONCRETE CLASSES -----------------
class Electronics(Item):
    def __init__(self, name, price, warranty_years):
        self.name = name
        self.price = price
        self.warranty_years = warranty_years

    def get_details(self):
        return f"Electronics: {self.name}, Price: {self.price}, Warranty: {self.warranty_years} years"


class Clothing(Item):
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size

    def get_details(self):
        return f"Clothing: {self.name}, Price: {self.price}, Size: {self.size}"


# ----------------- INVENTORY SYSTEM -----------------
class Inventory:
    total_items_ever_added = 0  # class variable

    def __init__(self):
        self.__items = []  # private list

    def add_item(self, item):
        self.__items.append(item)
        Inventory.total_items_ever_added += 1

    def remove_item(self, name):
        for item in self.__items:
            if item.name == name:
                self.__items.remove(item)
                return f"{name} removed"
        return "Item not found"

    def search_by_type(self, item_type):
        result = []
        for item in self.__items:
            if item_type == "Electronics" and isinstance(item, Electronics):
                result.append(item)
            elif item_type == "Clothing" and isinstance(item, Clothing):
                result.append(item)
        return result

    def total_value(self):
        total = 0
        for item in self.__items:
            total += item.price
        return total

    def display_all(self):
        for item in self.__items:
            print(item.get_details())

inv = Inventory()

e1 = Electronics("Laptop", 1000, 2)
e2 = Electronics("Phone", 700, 1)

c1 = Clothing("T-Shirt", 20, "M")
c2 = Clothing("Jeans", 50, "L")

inv.add_item(e1)
inv.add_item(e2)
inv.add_item(c1)
inv.add_item(c2)

print("---- All Items ----")
inv.display_all()

print("\nTotal Value:", inv.total_value())

print("\nElectronics Only:")
for item in inv.search_by_type("Electronics"):
    print(item.get_details())

print("\nTotal Items Ever Added:", Inventory.total_items_ever_added)