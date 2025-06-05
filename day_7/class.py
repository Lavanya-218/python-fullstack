class Student:
    name=" "
    rollno=0
    def display(self):
        print(f"{self.name} and rollno {self.rollno}")
a=Student()
a.name="Lavs"
a.rollno=21
a.display()