l=[]
n=int(input("Enter no.of elemnts:"))
for i in range(n):
    x=int(input())
    l.append(x)
for i in set(l):
    print(f"frequency of {i}=>{l.count(i)}")