#here we use property in banking system
class bankaccount:
    def __init__(self,balance=0):
        self.__balance=balance
    @property
    def balance(self):
        return self.__balance 
    def deposit(self,amount):
        if amount<0:
            print("invalid amount")
        else:
            self.__balance+=amount
    def withdraw(self,amount):
        if 0<amount<self.__balance:
             self.__balance -= amount
        else:
            print("invalid deposit amount")
s=bankaccount()
s.deposit(5000)
print(s.balance)
s.withdraw(2000)
print(s.balance)

    
