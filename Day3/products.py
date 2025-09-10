cart=[]
def e_comm():
    print("1.add\n 2.remove\n 3.search\n4.display\n5.total\6.Sort\n7.clear")
    while True:
        ch=int(input("Enter choice:"))
        if(ch==1):
         n=(input())
         cart.append(n)  
        elif ch==2:
             n=input("Enter delete element") 
             cart.remove(n)
        elif(ch==3):
            n=(input()) 
            print(cart.index(n))
        elif(ch==4):
            print(cart)
        elif(ch==5):
            print(len(cart))
        elif(ch==6):
            print(sorted(cart))
        elif(ch==7):
            print(cart.clear())
        else:
            print("Invalid choice")
            break
e_comm()