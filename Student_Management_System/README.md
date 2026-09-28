# Student Management System

A console-based **Student Management System** built with Python to practice and apply core Python programming concepts, including functions, data structures, exception handling, file handling, JSON, and Object-Oriented Programming (OOP).

## 📌 Features

* Add a new student
* View all students
* Search student by roll number
* Update student information
* Delete a student
* Validate student age
* Handle invalid input using exception handling
* Save student data permanently in a JSON file
* Load previously saved student data when the program starts

## 🛠️ Technologies Used

* Python
* JSON
* Object-Oriented Programming (OOP)

## 📂 Project Structure

```text
Student Management System/
│
├── main.py
└── students.json
```

> `students.json` is automatically created when student data is saved.

## 📋 Menu

```text
*** Student Management System ***

Choose option:
1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Update Student
6. Exit
```

## 🧠 Python Concepts Practiced

### 1. Classes and Objects

The project uses two classes:

* `Student` — represents a student.
* `StudentManagementSystem` — manages student records.

### 2. Constructor

The `__init__()` method initializes student and system data.

### 3. Lists

Student objects are stored in a list:

```python
self.students = []
```

### 4. Loops

`for` and `while` loops are used for:

* Displaying students
* Searching students
* Deleting students
* Validating age
* Running the menu continuously

### 5. Exception Handling

The program handles invalid age input using:

```python
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Invalid age")
```

It also handles:

* `FileNotFoundError`
* `json.JSONDecodeError`

### 6. File Handling

The `with open()` statement is used to read and write student data.

### 7. JSON

Student information is stored permanently in:

```text
students.json
```

The project uses:

```python
json.dump()
json.load()
```

### 8. CRUD Operations

The system implements the four basic CRUD operations:

| Operation | Function            |
| --------- | ------------------- |
| Create    | Add Student         |
| Read      | View/Search Student |
| Update    | Update Student      |
| Delete    | Delete Student      |

## 💾 Data Persistence

Student data is converted into dictionaries before being stored in JSON.

Example:

```json
[
    {
        "name": "Dikshya",
        "roll": "101",
        "age": 21
    }
]
```

When the program starts, the JSON data is loaded and converted back into `Student` objects.

## ▶️ How to Run

Make sure Python is installed.

Run the program from the terminal:

```bash
py student_management.py
```

Then select an option from the menu.

## 🎯 Purpose of the Project

This project was created as a practical learning project to strengthen Python fundamentals and combine multiple concepts into one real-world application.

It helped practice:

```text
Python Basics
     ↓
Functions
     ↓
Data Structures
     ↓
Exception Handling
     ↓
File Handling
     ↓
JSON
     ↓
OOP
     ↓
CRUD
     ↓
Data Persistence
```


## 👩‍💻 Author

**Dikshya Khanal**

Computer Engineering Student | Python Developer | AI/ML Aspiring
