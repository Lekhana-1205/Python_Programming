try:
    n=int(input())
    d=int(input())
    div=n/d
    print(d)
except ZeroDivisionError:
      print("Error:Division by zero is not allowed.")