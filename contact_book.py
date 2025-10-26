import re
contacts = []

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
            contact = {"name": name, "phone": phone, "email": email}
            contacts.append(contact)
            print(f"Contact {name} added!\n")
            break
        else:
            print("Invalid email entered\n")
def view_all_contacts():
    if not contacts:
        print("No contacts to show.\n")
        return
    print("All Contacts:")
    print("\n")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. Name: {c['name']}")
        print(f"   Phone: {c['phone']}")
        print(f"   Email: {c['email']}")
        print("\n")

while True:
    print("\n1. Add Contact\n2. View All Contacts\n3. Exit")
    choice = input("Choice: ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_all_contacts()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
