import os
from supabase import create_client, Client   # pip install supabase
from dotenv import load_dotenv               # pip install python-dotenv
#Load Environment Variables
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
# CRUD Operations
# 1. CREATE
def add_member():
    name = input("Enter member name: ")
    email = input("Enter member email: ")
    sb.table("members").insert({"name": name, "email": email}).execute()
    print(" Member added successfully!")

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    category = input("Enter category: ")
    stock = int(input("Enter stock: "))
    sb.table("books").insert({
        "title": title, "author": author,
        "category": category, "stock": stock
    }).execute()
    print("Book added successfully!")

# 2. READ
def list_books():
    result = sb.table("books").select("*").execute()
    print("\n Books Available:")
    for r in result.data:
        print(f"{r['book_id']}. {r['title']} by {r['author']} ({r.get('category','')}) - Stock: {r['stock']}")

def show_members():
    result = sb.table("members").select("*").execute()
    print("\n👥 Members:")
    for r in result.data:
        print(f"ID:{r['member_id']}, Name:{r['name']}, Email:{r['email']}")

# 3. UPDATE
def update_book_stock():
    book_id = int(input("Enter book ID: "))
    new_stock = int(input("Enter new stock: "))
    sb.table("books").update({"stock": new_stock}).eq("book_id", book_id).execute()
    print(" Book stock updated!")

def update_member_email():
    member_id = int(input("Enter member ID: "))
    new_email = input("Enter new email: ")
    sb.table("members").update({"email": new_email}).eq("member_id", member_id).execute()
    print(" Member email updated!")

# 4. DELETE
def delete_member():
    member_id = int(input("Enter member ID: "))
    sb.table("members").delete().eq("member_id", member_id).execute()
    print("ℹ Member deleted (if no borrowed books).")

def delete_book():
    book_id = int(input("Enter book ID: "))
    sb.table("books").delete().eq("book_id", book_id).execute()
    print("ℹBook deleted (if not borrowed).")

def main():
    while True:
        print("\n Library Management System")
        print("1. Create (Add Member / Add Book)")
        print("2. Read (List Books / Show Members)")
        print("3. Update (Book Stock / Member Email)")
        print("4. Delete (Member / Book)")
        print("5. Exit")

        choice = input("Enter option: ")

        if choice == "1":
            sub = input(" Add (m)ember or (b)ook? ")
            if sub.lower() == "m":
                add_member()
            else:
                add_book()

        elif choice == "2":
            sub = input(" Show (b)ooks or (m)embers? ")
            if sub.lower() == "b":
                list_books()
            else:
                show_members()

        elif choice == "3":
            sub = input(" Update (s)tock or (e)mail? ")
            if sub.lower() == "s":
                update_book_stock()
            else:
                update_member_email()

        elif choice == "4":
            sub = input(" Delete (m)ember or (b)ook? ")
            if sub.lower() == "m":
                delete_member()
            else:
                delete_book()

        elif choice == "5":
            print(" Exiting...")
            break

        else:
            print("Invalid option! Try again.")

if __name__ == "__main__":
    main()