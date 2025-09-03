def checkAlphabet(c):
    st="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    if(c in st):
        print("Is alphabet")
    else:
        print("not an alphabet")
a=input()
print(checkAlphabet(a))