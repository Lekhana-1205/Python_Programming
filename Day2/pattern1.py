n=int(input())
def starPrint(n):
    for i in range(n):
        for j in range(n):
               print("*",end=" ")
        print()
starPrint(n)