import gradefunction as g
grade_book={}
print("Maintaining student gradebook:\n")
while True:
    print("The choices:")
    print("1.Add student")
    print("2.View students,marks along with average")
    print("3.Searching the Student")
    print("4.To remove the student")
    print("5. To upadte the data")
    print("6.exit")
    choice=int(input("Enter the choice:"))
    if choice==1:
        g.add_student(grade_book)
    elif choice==2:
        g.view_student(grade_book)
    elif choice==3:
        g.search_student(grade_book)
    elif choice==4:
        g.remove_student(grade_book)
    elif choice==5:
        g.update_student(grade_book)
    else:
        print("Exit")
        break

