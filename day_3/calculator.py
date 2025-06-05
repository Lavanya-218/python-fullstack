import funtions_module
#import funtions_module as lav # lav.add
#from funtions_module import add # add
n1=int(input("Enter a number:"))
while True:
    oper=input("Enter operator:")
    if oper=="=":
        print("result:",n1)
        break
    n2=int(input("Enter another number:"))
    if oper=="+":
        n1=funtions_module.add(n1,n2)
    elif oper=="-":
        n1=funtions_module.sub(n1,n2)
    elif oper=="*":
        n1=funtions_module.mul(n1,n2)
    elif oper=="/":
        n1=funtions_module.div(n1,n2)
    elif oper=="%":
        n1=funtions_module.mod(n1,n2)
    elif oper=="**":
        n1=funtions_module.pow(n1,n2)
    else:
        print("Enter a valid arithmetic operator")
    print(n1)