print("*** Student Management System ***")

while True: 
    print("choose option:")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        print("Add Student selected")

    elif choice == "2":
        print("View Students selected")

    elif choice == "3":
        print("Search Student selected")

    elif choice == "4":
        print("Delete Student selected")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")