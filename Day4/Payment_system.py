class Payment:
    def pay(self,amount):
        print(f"Paid {amount}")
class CashPayment(Payment):
    def pay(self,amount):
        print(f"Paid ₹<{amount}> in cash")
class CardPayment(Payment):
    def pay(self,amount):
        print(f"Paid ₹<{amount}> using credit/debit card")
class UPIPayment(Payment):
    def pay(self,amount):
        print(f"Paid ₹<{amount}> using UPI")
cash=CashPayment()
card=CardPayment()
upi=UPIPayment()
l=[cash,card,upi]
for i in l:
    i.pay(1000)