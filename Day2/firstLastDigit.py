n = int(input("Enter a number: "))
def firstLastDigits(n):
    s = str(abs(n)) 
    print("First digit:", s[0])
    print("Last digit:", s[-1])

firstLastDigits(n)
