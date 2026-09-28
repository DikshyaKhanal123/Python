print("*** Student Management System ***")

students = []

while True: 
    print("choose option:")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
       name = input("Enter Student name:") 
       roll = input("Enter roll number:")
       age = input("Enter age:")
       student = {
    "name" : name,
    "roll" : roll,
    "age" : age
}

       students.append(student)
       print("student added successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                print(student)

    elif choice == "3":
    
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

    elif choice == "4":

        roll = input("Enter roll number to delete: ")

        for student in students:
            if student["roll"] == roll:
                students.remove(student)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found!")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")