# Build an ATMAccount class with a private attribute __balance and __pin. Write getter and setter methods. The setter for balance should reject negative values. Add a verify_pin(pin) method and a withdraw(amount, pin) method that only works if the pin is correct AND balance is sufficient.
# Balance and pin stored as private (__balance, __pin)
# get_balance() and set_balance() methods
# withdraw() must verify pin first, then check balance
# Print appropriate error messages for wrong pin or insufficient funds



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


