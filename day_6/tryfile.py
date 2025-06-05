try:
    file=open("day_6/trytxt.txt","a")
    num=int(input("Enter an number:"))
    f=1
    for i in range(1,num+1):
        f=f*i
    #print("Factorial:",f)
except Exception as e:
    print(f"The error is {e}")
else:
    file.write("The Factorial is :",f)
finally:
    print("Finally done the code")

