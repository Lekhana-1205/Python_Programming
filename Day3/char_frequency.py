'''s=input("Enter the string:")
for ch in set(s):
    print(f"{ch}{s.count(ch)}",end="")
'''
s=input("Enter the string: ")
seen=set()
result=""
for ch in s:
    if ch not in seen:
        count=s.count(ch)
        result += ch + str(count)
        seen.add(ch)
print(result)

