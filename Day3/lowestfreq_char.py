s=input("Enter string:")
c=min(set(s), key=s.count)
print(c,s.count(c))
