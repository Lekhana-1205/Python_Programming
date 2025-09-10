ec=0
oc=0
l=[]
e=[]
o=[]
n=int(input())
for i in range(n):
        x=int(input())
        l.append(x)
        if(l[i]%2==0):
            ec+=1
            e.append(l[i])
        else:
            oc+=1
            o.append(l[i])
print(f"even list:{e},even count:{ec}")
print(f"odd count:{oc} odd list{o}")
