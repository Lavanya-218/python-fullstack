op1=int(input("Enter a number:"))
op2=int(input("Enter a number:"))
op=input("Enter an operator:")
o=["+","-","*","/","%"]
for i in o:
    if op=="+":
        print(op1+op2)
        break
    elif op=='-':
        print(op1-op2)
        break
    elif op=="*":
        print(op1*op2)
        break
    elif op=="/":
        print(op1/op2)
        break
    elif op=="%":
        print(op1%op2)
        break
else:
    print("Enter an valid operator")
