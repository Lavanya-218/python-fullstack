# class Student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#     def display(self):
#         print(f"{self.name} and the rollno {self.rollno}")

# a=Student("lavs","5b6")
# a.display()
# b=Student("deepu",575)
# b.display()
# c=Student("niha","5b4")
# c.display()

class Person:
  surname="vasamsetti" #default parameter
  def __init__(self, name):
    self.name = name

  def change_name(self, new_name):
    self.name = new_name

  def show_name(self):
    print(f"My name is {self.name}")

  def __str__(self): # if we try to print object it gives the address so to handle it we __str__
    return f"object name is {self.surname}"


p=Person("niha")
p.change_name("lavanya")
p.show_name()
print(p.surname)
print(p)