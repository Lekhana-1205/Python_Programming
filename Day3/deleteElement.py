l=[]
n=int(input())
for i in range(n):
    x=int(input())
    l.append(x)
x=int(input("Enter delete position:"))
del l[x]
print(l)