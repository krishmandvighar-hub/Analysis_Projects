import math
student ={}
student_ids =set()

def calculate_grade(p):
    if p >= 75:
        return "A"
    elif p >= 60:
        return "B"
    elif p >= 40:
        return "C"
    else:
        return "fail"
def add_student():
    try:
        student_id=int(input("enter student id: "))
        if student_id in student_ids:
            print("student Already exist")
            return
        name = input("enter name")
        subj =("phy","chem","math")
        marks =[]

        for x in subj:
            m = int(input(f"enter{x}: "))
            marks.append(m)
        total=sum(marks)
        percentage=total/len(subj)
        percentage=math.ceil(percentage)
        grade=calculate_grade(percentage)

        student[student_id]={
            "name":name,
            "marks":tuple(marks),
            "percentage":percentage,
            "grade":grade
        }
        student_ids.add(student_id)
        print("student added successfully")
    except ValueError:
        print("invalid!,please enter number only")
    finally:
        print("return")
        
def dis():
    if not student:
        print("no student found")
        return
    for a,b in student.items():
        print(f"ID: {a}")
        print(f"Name: {b['name']}")
        print(f"Marks: {b['marks']}")
        print(f"Percentage: {b['percentage']}")
        print(f"Grade: {b['grade']}")

def menu():
    print("\n....Student Management System")
    print("1. Add student")
    print("2. Display Student")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
        menu()
    elif choice == "2":
        dis()
        menu()
    elif choice == "3":
        print("YOU DID IT WELL")
    else:
        print("Invalid choice")
        menu()

menu()
