import re
import json
import os
contacts = []
#checking if JSON file exists
if os.path.exists("contacts.json"):
    with open("contacts.json","r")as f:
        try:
            contacts=json.load(f)
        except json.JSONDecodeError:
                    contacts=[]
                    print("Unable to read contents of the file\n")
else:
     print("file not found\n")
#adding new contact....
def add_contact():
    name = input("Enter name: ")
    while True:
        phone = input("Enter phone number: ").strip()
        if(len(phone)==10):
            if re.match(r'^[7-9][0-9]{9}$',phone):
                print("Valid phone number\n")
                break
            else:
                print("Invalid phone number\n")  
        else:
            print("Invalid phone number\n")
    while True:
        email = input("Enter email: ").strip()
        email_pattern=r'^[-A-Za-z0-9_.]+@(gmail|yahoo)\.com$'
        if re.match(email_pattern,email):
            contact = {"Name": name, "Phone": phone, "Email": email}
            contacts.append(contact)
            with open ("contacts.json","w") as f:
                json.dump(contacts,f,indent=4)
            print(f"Contact {name} added!\n")
            break
        else:
            print("Invalid email entered\n")
#Viewing contacts....
def view_all_contacts():
    if not contacts:
        print("No contacts to show.\n")
        return
    print("All Contacts:")
    print("\n")
    for cont in contacts:
            print("-" * 30)
            print(f"Name: {cont['Name']}")
            print(f"Phone: {cont['Phone']}")
            print(f"Email: {cont['Email']}")
    print("-" * 30)
#Contact Book Menu....
while True:
    print("\n1. Add Contact\n2. View All Contacts\n3. Exit")
    choice = input("Choice: ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_all_contacts()
    elif choice == '3':
        print("Closing Contact Book...\n")
        break
    else:
        print("Invalid choice. Try again.")
