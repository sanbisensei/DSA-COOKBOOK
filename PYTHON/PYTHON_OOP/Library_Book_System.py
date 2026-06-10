# Library Book System
# Create a class Book with attributes title, author, and is_available (default True). Add methods checkout() and return_book() that toggle availability and print a status message. Create 3 book objects and simulate a checkout flow.
# __init__ with 3 attributes
# checkout() sets is_available to False and prints 'Book checked out'
# return_book() sets is_available to True and prints 'Book returned'
# Handle case where someone tries to checkout an already-checked-out book



class Book:
    def __init__(self,title,author,is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available
        

    def checkout(self):
        if self.is_available:
            self.is_available = False
            print("Book checked Out")
        else:
            print("Book is already borrowed")

    def return_book(self):
        self.is_available = True
        print("Book returned")

    
book1 = Book("homophobia","Imran Hossain", True)
book1 = Book("GayWar","MAshrafi", True)
book1 = Book("ManChild","Noor", True)

book1.checkout()
book1.checkout()
book1.return_book()
book1.checkout()
