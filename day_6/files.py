file=open("day_6/sample.txt","r")
#file.writelines("Lavs=2345555\nDeepu=34455577\nNiha=4573838")
#print(file.read())
data=file.read()
#print(data) #the ouput:
# Lavs=2345555
# Deepu=4455577
# Niha=4573838
list_data=data.split("\n")
# #print(list_data) the output:['Lavs=2345555', 'Deepu=4455577', 'Niha=4573838']
contact={}
for item in list_data:
#     #print(item) The output:
#     # Lavs=2345555
#     # Deepu=4455577
#     # Niha=4573838
    sp_key=item.split("=")
    #print(sp_key) #The output:
# #    ['Lavs',2345555']
# #    ['Deepu','4455577']
# #    ['Niha','4573838']
    contact[sp_key[0]]=sp_key[1]
print(contact)

