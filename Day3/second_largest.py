list=[]
n=int(input())
for i in range(n):
    x=int(input())
    list.append(x)
maxi=list[0]
smax=list[0]
for i in range(1,n):
    if(list[i]>maxi):
        smax=maxi
        maxi=list[i]
    elif(list[i] < maxi and list[i] > smax):
        smax=list[i]
print("second largest:",smax)


