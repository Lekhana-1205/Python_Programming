s1=input("Enter string1:")
s2=input("Enter string2:")
def length(s):
    c=0
    for ch in s:
        c+=1
    print("length:",c)
def comp(s1,s2):
    if(s1==s2):
        print("Both the strings are same")
    else:
        print("Both the strings are not same")
def concat(s1,s2):
    s=s1+s2
    print("Concatenated string:",s)
length(s1)
length(s2)
comp(s1,s2)
concat(s1,s2)