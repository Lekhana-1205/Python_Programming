def is_perfect(n):
    if n <= 0:
        return False
    sum_div = 0
    for i in range(1, n):
        if n % i == 0:
            sum_div += i
    return sum_div == n
num = int(input("Enter a number: "))
if is_perfect(num):
    print(f"{num} is a Perfect Number")
else:
    print(f"{num} is Not a Perfect Number")
