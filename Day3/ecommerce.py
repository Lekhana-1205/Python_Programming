cart=[]
def ecomme():
    print(" 1.Add\n 2.Remove\n 3.Search\n 4.Display\n 5.Total \n 6.Sort\n 7.Clear\n 8.Exit")
    while True:
        n=int(input("Enter your choice:"))
        if n==1:
            p=input("Enter product name: ")
            cart.append(p)
            print(p,"added to cart.")
        elif n==2:
            p1=input("Enter product name to remove: ")
            if p1 in cart:
                cart.remove(p1)
                print(p1,"removed from cart.")
            else:
                print("Product not found in cart.")
        elif n==3:
            p2=input("Enter product name to search: ")
            if p2 in cart:
                print("Product found:",p2)
            else:
                print("Not found.")
        elif n==4:
            if cart:
                print("Products in cart:",cart)
            else:
                print("Cart is empty.")
        elif n==5:
            print("Total products in cart:",len(cart))
        elif n==6:
            print("Sorted products:",sorted(cart))
        elif n==7:
            cart.clear()
            print("Cart cleared!")
        elif n==8:
            print("Exiting...!")
            break
        else:
            print("Invalid choice.")

ecomme()
