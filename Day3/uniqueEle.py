l=[]
n=int(input())
for i in range(n):
    x=int(input())
    l.append(x)
print("list",l)
s=set(l)
l=list(s)
print("unique elements:",l)
