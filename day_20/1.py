a=input()
print(a)
s=a[1:len(a)-1]
#l=list(s)
# if '@' in s:
#     if '.' in s:
#         print("valid")
#     else:
#         print("Invalid")
# else:
#     print("Invalid")

if '@' in s and '.' in s:
    print("valid")
else:
    print("invalid")