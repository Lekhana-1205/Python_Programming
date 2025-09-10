l=[]
d=[]
n=int(input())
for i in range(n):
    x=(input())
    l.append(x)
for x in set(l):
    if l.count(x) > 1:
        d.append(x)
print(d)
