class ATMAccount:
    def __init__(self,balance,pin):
        self.__balance = balance
        self.__pin = pin

    def get_balance(self):
        return self.__balance
    
    
    
    def set_balance(self,balance):
        if self.__balance >= 0:
           self.__balance = balance
        else:
            return "Negative Value"

    
    def Verify_pin(self,pin):
        return pin == self.__pin

    def withdraw(self,amount,pin):
         if self.Verify_pin(pin) == False:
             return "Error: wrong Pin"
         if amount > self.__balance:
             return "Error: not enough balance"
         
         else:
            self.__balance -= amount
         return f"Withdraw successful. Remaining balance: {self.__balance}"

one = ATMAccount(1200, 555)

print(one.withdraw(500, 555))


