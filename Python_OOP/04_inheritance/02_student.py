class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):

    def __init__(self, name, age, roll, course):
        self.name = name
        self.age = age
        self.roll = roll
        self.course = course

    def display_student(self):
        print("Roll:", self.roll)
        print("Course:", self.course)


# Creating Student object
student1 = Student("Dikshya", 19, 10, "Computer Engineering")

# Calling inherited method
student1.display_person()

# Calling Student's own method
student1.display_student()