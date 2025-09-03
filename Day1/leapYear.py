def LeapYear(y):
    if(y%4==0):
        print("Leap year")
    else:
        print("Not a leap year")
a=int(input())
print(LeapYear(a))