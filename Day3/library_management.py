
d={}
def lib():
    print("\n1.Add\n2.Remove\n3.Search\n4.Update\n5.Display\n6.Total\n7.isExist\n8.Exit")
    while True:
        ch=int(input("Enter choice:"))
        if ch==1:
            k=input("Enter book id:")
            v=input("Enter book title:")
            d[k]=v
            print("Book added successfully.")
        elif ch==2: 
            k=input("Enter book id to remove:")
            if k in d:
                d.pop(k)
                print("Book removed successfully.")
            else:
                print("Book ID not found.")
        elif ch==3: 
            k=input("Enter book id to search:")
            if k in d:
                print(f"Book found:{d[k]}")
            else:
                print("Book ID not found.")  
        elif ch==4:
            k=input("Enter book id to update:")
            if k in d:
                v=input("Enter new book title:")
                d[k]=v
                print("Book updated successfully.")
            else:
                print("Book ID not found.")
        elif ch==5: 
            if d:
                print("All books in library:")
                for key,value in d.items():
                    print(f"{key}:{value}")
            else:
                print("Library is empty.")
        elif ch==6:
            print("Total number of books:",len(d))
        
        elif ch==7: 
            v=input("Enter book title to check:")
            if v in d.values():
                print("It exists.")
            else:
                print("It does not exist.")
        elif ch==8: 
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

lib()
