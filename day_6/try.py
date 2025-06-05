try:
    num=int(input("Enter an number:"))
    f=1
    for i in range(1,num+1):
        f=f*i
     #print("The Factorial is :",f)
# except ValueError:
#     print("The error has happened as ValueError")
except Exception as e:
    print(f"The error is {e}")
else:
    print("The Factorial is :",f)
finally:
    print("Finally done the code")
