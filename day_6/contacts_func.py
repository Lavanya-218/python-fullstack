
def add_contact(contacts):
    name = input("Enter Contact Name :")
    mobile = int(input("Enter mobile number :"))
    file=open("day_6/contactsfile.txt","a")
    file.write(f"{name}={mobile}\n")
    file.close()


def view_contacts(contacts):
    file=open("day_6/contactsfile.txt","r")
    p=file.readlines()
    if not p:
        print("No data")
    else:
        for i in p:
            # contact=i.split(",")
            # print(f"{contact[0]},{contact[1]}")
            print(i.strip("\n"))
    file.close()


def delete_contact(contacts):
    file=open("day_6/contactsfile.txt","r")
    p=file.readlines()
    file.close()
    name_to_delete = input("Enter contact name to delete :")
    delete=False
    file = open("day_6/contactsfile.txt", "w")
    for key in p:
        name=key.split("=")
        if name_to_delete==name[0]:
            delete=True
            continue
        else:
            file.write(key)
    if not delete:
        print(f"The {name_to_delete} contact not found")
    else:
         print(f"The contact {name_to_delete} is deleted")
    file.close()


def find_contact(contacts):
    query = input("Enter name to search : ").lower()
    found=False
    file=open("day_6/contactsfile.txt","r")
    p=file.readlines() 
    for key in p:
        if query in key.lower():
            print(key.strip("\n"))
            found=True
    if not found:
        print("No data of your requirement")
    file.close()

   
def edit_contact(contacts):
    file = open("day_6/contactsfile.txt", "r")
    p = file.readlines()
    file.close()
    name_to_edit = input("Enter contact name to edit: ").lower()
    number = int(input("Enter the number: "))
    edit=False
    file = open("day_6/contactsfile.txt", "w") 
    for key in p:
        name=key.split("=")
        #print(name)
        if name_to_edit == name[0]:
            file.write(f"{name_to_edit}={number}\n")
            edit=True
        else:
            file.write(key)
    if not edit:
        print("contact not found")
    file.close()
