def slug_generator(string):
    str=""
    for i in string:
        if i==' ':
            str=str+'-'
            continue
        elif i.isalnum():
            str=str+i
        else:
            continue

    return str.lower()

title=input()
result=slug_generator(title)
print(result)


# def slug_generator(x):
#     x=x.lower()
#     x=list(x)
#     result=""
#     for i in range(0,len(x)):
#         if x[i].isalnum():
#             result+=x[i]
#         elif x[i]==" ":
#             result+='-'
#         else:
#             continue
#     return result
# title=input()
# print(slug_generator(title))