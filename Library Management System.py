#!/usr/bin/env python
# coding: utf-8

# In[5]:


books = {}
user = {}

def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    copies = int(input("Enter the number of copies available: "))
    books[title] = {"author": author, "copies": copies}
    print(f"Book '{title}' has been added to the library.")

def check_out_book():
    title = input("Enter the title of the book you want to check out: ")
    if title in books and books[title]["copies"] > 0:
        user_id = input("Enter your user ID: ")
        if user_id in patrons:
            user[user_id]["checked_out_books"].append(title)
            books[title]["copies"] -= 1
            print(f"Book '{title}' has been checked out to user {patron_id}.")
        else:
            print("Invalid user ID.")
    else:
        print("Book not available or does not exist in the library.")

# Function to check in a book
def check_in_book():
    title = input("Enter the title of the book you want to return: ")
    user_id = input("Enter your patron ID: ")
    if user_id in user and title in user[user_id]["checked_out_books"]:
        user[user_id]["checked_out_books"].remove(title)
        books[title]["copies"] += 1
        print(f"Book '{title}' has been returned by User {user_id}.")
    else:
        print("Book not checked out by this user or user ID is invalid.")

def add_user():
    user_id = input("Enter a unique user ID: ")
    if user_id not in user:
        name = input("Enter the user's name: ")
        user[user_id] = {"name": name, "checked_out_books": []}
        print(f"User {user_id} ({name}) has been added.")
    else:
        print("User ID already exists. Please choose a unique ID.")

# Main program loop
while True:
    print("\nLibrary Management System Menu:")
    print("1. Add a Book")
    print("2. Check Out a Book")
    print("3. Check In a Book")
    print("4. Add a User")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        check_out_book()
    elif choice == "3":
        check_in_book()
    elif choice == "4":
        add_user()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please select a valid option.")

print("Goodbye! Thank you for using the Library Management System.")


# In[ ]:





# In[ ]:




