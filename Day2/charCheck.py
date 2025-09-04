def charCheck(c):
    if(c.isalpha()):
        print("c is a Character")
    elif(c.isdigit()):
        print("c is a digit")
    else:
        print("c is a special character")
c=input("Enter the input:")
charCheck(c)