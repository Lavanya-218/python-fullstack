posts=[
    {"user":"alice","post":"hi"},
    {"user":"bob","post":"hello"},
    {"user":"alice","post":"again"},
    {"user":"x","post":"xyz"},
    {"user":"bob","post":"again"}
]
new_dic={}
for i in posts:
    if i["user"] in new_dic:
        new_dic[i["user"]]=new_dic[i["user"]]+1
    else:
        new_dic[i["user"]]=1
print(new_dic)

    

    
