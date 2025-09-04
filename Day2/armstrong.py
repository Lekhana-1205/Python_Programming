n=int(input())
def armstrong(n):
    sum=0
    t=n
    while(t>0):
        rem=t%10
        sum=sum+(rem*rem*rem)
        t=t//10
    if(sum==n):
        print("Armstrong")
    else:
        print("Not an armstrong")
armstrong(n)