n = int(input("Enter a number: "))

def prime(n):
    if n <= 1:
        print("Not prime")
        return
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not prime")
            return
    print("Prime")

prime(n)
