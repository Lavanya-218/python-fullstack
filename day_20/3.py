# list=input().split(" ")
# print(list)
# query=input("Enter the word to search:")
# newlist=[]
# flag=False
# for i in list:
#     if query.lower() in i.lower():
#         newlist.append(i)
#         flag=True
# if not(flag):
#     print("no data")
# else:
#     print(newlist)

n=int(input("Enter no.of elements:"))
list=[]
for i in range(n):
    a=input("Enter the data:")
    list.append(a)
print(list)
query=input("Enter the word to search:")
newlist=[]
flag=False
for i in list:
    if query.lower() in i.lower():
        newlist.append(i)
        flag=True
if not(flag):
    print("no data")
else:
    print(newlist)