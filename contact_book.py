contacts=[]
def add_contact():
    name=input("Enter name:")
    phone_number=int(input("Enter the contact number:"))
    email=input("Enter the email address:")
    contacts.append([name,phone_number,email])
print("Contact successfully added\n")
def view_contact():
    if len(contacts)==0:
        print("No contacts to display\n")
    else:
        print("---Dispalying Contact Book---\n")
        for i in contacts:
            print("Name:",i[0],"\tContact Number:",i[1],"\tEmail:",i[2])
while ch!='3':
    print("---Menu---\n")
    print("1.Add contact\n2.View all contacts\n3.Exit\n")
    ch=input("Enter your choice:")
    if ch=='1':
        add_contact()
    elif ch=='2':
        view_contact()
    elif ch=='3':
        print("Exiting program...\n")
        break
    else:
        print("Invalid choice entered!!!\n")