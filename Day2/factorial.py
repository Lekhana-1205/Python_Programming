n=int(input("Enter number"))
def factorial(n):
    fact=1
    i=1
    while(i<=n):
        fact*=i
        i+=1
    print(fact)
factorial(n)