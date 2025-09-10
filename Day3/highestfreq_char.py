s=input("Enter string:")
c=max(set(s), key=s.count)
print(c,s.count(c))
