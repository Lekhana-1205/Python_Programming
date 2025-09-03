def greaterof3(a,b,c):
    if(a>b):
        if(b>c):
            print("b is greater")
        else:
            print("c is greater")
    else:
        if(b>c):
            print("b is greater")
        else:
            print("c is greater")
a=int(input())
b=int(input())
c=int(input())
greaterof3(a,b,c)