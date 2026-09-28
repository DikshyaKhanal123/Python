import json

print("*** Student Management System ***")


class Student:
    def __init__(self, name, roll, age):
        self.name = name
        self.roll = roll
        self.age = age


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter Student name: ")
        roll = input("Enter roll number: ")

        while True:
            try:
                age = int(input("Enter age: "))

                if age <= 0:
                    raise ValueError("Age must be greater than 0")

                break

            except ValueError as e:
                print(e)

        student = Student(name, roll, age)

        self.students.append(student)

        print("Student added successfully!")

    def view_students(self):
        if len(self.students) == 0:
            print("No students found.")
        else:
            for student in self.students:
                print(f"Name: {student.name}")
                print(f"Roll: {student.roll}")
                print(f"Age: {student.age}")
                print()

    def search_student(self):
        roll = input("Enter roll number to search: ")

        for student in self.students:
            if student.roll == roll:
                print("Student found!")
                print(f"Name: {student.name}")
                print(f"Roll: {student.roll}")
                print(f"Age: {student.age}")
                break
        else:
            print("Student not found!")

    def delete_student(self):
        roll = input("Enter roll number to delete: ")

        for student in self.students:
            if student.roll == roll:
                self.students.remove(student)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found!")

    def save_students(self):
        data = []

        for student in self.students:
            data.append({
                "name": student.name,
                "roll": student.roll,
                "age": student.age
            })

        with open("students.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Students saved successfully!")

    def load_students(self):
        try:
            with open("students.json", "r") as file:
                data = json.load(file)

                for item in data:
                    student = Student(
                        item["name"],
                        item["roll"],
                        item["age"]
                    )

                    self.students.append(student)

        except FileNotFoundError:
            print("No saved student data found.")

        except json.JSONDecodeError:
            print("Invalid JSON data found.")

    def update_student(self):
        roll = input("Enter roll number to update: ")

        for student in self.students:
            if student.roll == roll:
                print("Student found!")

                name = input("Enter new name: ")
                
                while True:
                    try:
                        age = int(input("Enter new age: "))

                        if age <= 0:
                            raise ValueError("Age must be greater than 0")

                        break

                    except ValueError as e:
                        print(e)

                student.name = name
                student.age = age

                print("Student updated successfully!")
                return

        print("Student not found!")


system = StudentManagementSystem()

system.load_students()

while True:
    print("\nChoose option:")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        system.add_student()
        system.save_students()

    elif choice == "2":
        system.view_students()

    elif choice == "3":
        system.search_student()

    elif choice == "4":
        system.delete_student()
        system.save_students()

    elif choice == "5":
        system.update_student()
        system.save_students()


    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")