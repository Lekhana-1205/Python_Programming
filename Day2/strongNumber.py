def fact(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f 

def strongNumber(n):
    sum = 0
    t = n
    while t > 0:
        r = t % 10
        sum += fact(r)
        t //= 10
    if sum == n:
        print(f"{n} is a Strong Number")
    else:
        print(f"{n} is Not a Strong Number")
        
s = int(input("Enter a number: "))
strongNumber(s)
