d=int(input("Enter no.of days:"))
def daysToYears(x):
    months=(x/30)
    years=x/365
    print(f"Months:{months},Years:{years}")   
daysToYears(d)