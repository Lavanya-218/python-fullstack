def validate_email(email):
    l=['`','!','#','$','%','^','*','(',')',',',':',';','{','}','[',']','=','-','+','_']
    for i in l:
        if i in email:
            return False
    else:
        if '@' in email and '.' in email:
            return True
    # else:
    #     return False
    
a=input()
a=a[1:len(a)-1]
print(validate_email(a))