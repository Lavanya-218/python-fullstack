def add_student(grade_book):
    name=input("Enter the name: ")
    marks=list(map(int,input("Enter the marks:").split()))
    grade_book[name]=marks

def view_student(grade_book):
    # for i in grade_book:
    #     s=0
    #     for j in grade_book[i]:
    #        s=s+j
    #     avg=s/len(grade_book[i])
    #     print(f"{i}:{j},avg:",avg)
    if not grade_book:
        print("no data")
    for i,j in grade_book.items():
        avg=sum(j)/len(j)
        print(f"{i} Marks:{j} and Avg= {avg:.3f}")


def search_student(grade_book):
    name_search=input("Enter the name to search:")
    for i,j in grade_book.items():
        if name_search==i:
            avg=sum(j)/len(j)
            print(f"{i} Marks:{j} and Avg= {avg:.3f}")
            break
    else:
        print("Not found")

def remove_student(grade_book):
    name=input("Enter the name to be removed:")
    if name in grade_book:
        del grade_book[name]
        print(f"{name} removed")
    else:
        print("name doesn't exist")

def update_student(grade_book):
    name=input("Enter the name: ")
    if name in grade_book:
        marks=list(map(int,input("Enter the marks:").split()))
        grade_book[name]=marks
    else:
        print("cannot upadte")


