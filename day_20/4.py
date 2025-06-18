n=int(input("Enter the noof users:"))
user_list=[]
for i in range(n):
    dic={}
    # Name=input("ENter name:")
    # id=int(input("Enter id:"))
    # dic["Name"]=Name
    # dic["id"]=id
    dic["Name"]=input("Enter name:")
    dic["id"]=int(input("Enter id:"))
    user_list.append(dic)
print(user_list)
query=input("Enter the name:")
new_list=[]
flag=False
for i in user_list:
    if query.lower() in i["Name"].lower():
        new_list.append(i)
        flag=True

    # if query==i["Name"]:
    #     print(i)
    #     break
if not(flag):
    print("no data")   
else:
    print(new_list)