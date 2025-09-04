n=int(input())
def palindrome(n):
    rev=0
    t=n
    while(t>0):
        rem=t%10
        rev=rev*10+rem
        t=t//10
    if(rev==n):
        print("Palindrome")
    else:
        print("Not an Palindrome")
palindrome(n)