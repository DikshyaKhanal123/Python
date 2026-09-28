print("*** Student Management System ***")

students = []

def  add_student():
    name = input("Enter Student name:") 
    roll = input("Enter roll number:")
    while True:
        try:
            age = int(input("Enter age:"))
            if age <= 0:
                raise ValueError("Age must be greater than 0")
            break
        except ValueError as e:
            print(e)
        

    student = {
        "name" : name,
        "roll" : roll,
        "age" : age
    }
    
    students.append(student)
    print("student added successfully!")

def view_students():
    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            print(student)

def search_student():
    roll = input("Enter roll number to search: ")
    
    for student in students:
        if student["roll"] == roll:
            print("Student found!")
            print(f"Name: {student['name']}")
            print(f"Roll: {student['roll']}")
            print(f"Age: {student['age']}")
            break
    else:
        print("Student not found!")

def delete_student():
    roll = input("Enter roll number to delete: ")
    
    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student deleted successfully!")
            break
    else:
        print("Student not found!")
    
while True: 
    print("choose option:")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()
    
    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
