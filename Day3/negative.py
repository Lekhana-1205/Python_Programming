list=[]
l=[]
n=int(input())
for i in range(n):
    x=int(input())
    list.append(x)
    if(list[i]<0):
      l.append(list[i])
print(l)
