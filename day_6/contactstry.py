import contacts_func as c
contacts = {}
print("\tContacts App")
while True:
    try:
        print("Choices :")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Delete contact")
        print("4. Find contact")
        print("5. Edit contact")
        print("6. Exit")
        choice = int(input("Enter choice : "))

        if choice == 1:
            c.add_contact(contacts)
        elif choice == 2:
            c.view_contacts(contacts)
        elif choice == 3:
            c.delete_contact(contacts)
        elif choice == 4:
            c.find_contact(contacts)
        elif choice == 5:
            c.edit_contact(contacts)
        else:
            print("Thank You ")
            break
    except Exception as e:
        print(f"The error is {e}")
    else:
        print("The contacts App")
    finally:
        print("Finally done the code")
