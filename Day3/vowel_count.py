s=input("Enter the string:")
v="aeiouAEIOU"
cc=vc=0
for c in s:
    if c in v:
        vc+=1
    else:
        cc+=1
print("Vowel count:",vc)
print("Consonent count:",cc)