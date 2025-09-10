ac = dc = sc = 0
s = input("Enter the string: ")
for c in s:
    if c.isalpha():
        ac += 1
    elif c.isdigit():
        dc += 1
    else:
        sc += 1
print("Alphabet count:", ac)
print("Digit count:", dc)
print("Special character count:", sc)