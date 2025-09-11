class BankAccount:
    def __init__(self):
        self.__balance=0
    def deposit(self,amount):
        self.__balance=amount+self.__balance
        print(f"Deposit ₹{amount}")
    def withdraw(self,amount):
        self.__balance-=amount
        print(f"Withdraw ₹{self.__balance}")
    def get_balance(self):
        return self.__balance
b=BankAccount()
b.deposit(5000)
b.withdraw(2000)
b.get_balance