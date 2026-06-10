# Build a mini shopping system. Create a class Product with name, price, and stock. Create a class Cart that holds a list of products. Cart should have: add_product(product), remove_product(name), total_price(), and checkout() which prints all items and the total. The add_product() should check if stock > 0 before adding.

# Cart stores products in a list

# remove_product() loops through the list to find by name

# total_price() uses a for loop to sum prices

# checkout() loops through and prints each item's name and price, then prints the total

# Buying a product reduces its stock by 1



class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock
    

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self,product):
        if product.stock>0:
            self.products.append(product)
            product.stock -=1
            print(f"{product.name} added to cart")
        else:
            print(f"{product.name} is out of stock")
    
    def remove_product(self,name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                product.stock+=1
                print(f"{name} removed from cart")
                return
        print(f"{name} not found in cart")


    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return total
    
    def checkout(self):
        print("\n--- Checkout ---")
        for product in self.products:
            print(f"{product.name}: {product.price}")
        print("Total:", self.total_price())


p1 = Product("Laptop", 1000, 2)
p2 = Product("Mouse", 50, 5)
p3 = Product("Keyboard", 80, 1)

cart = Cart()

cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)

cart.remove_product("Mouse")

cart.checkout()