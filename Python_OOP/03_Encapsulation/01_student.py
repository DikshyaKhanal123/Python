class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display(self):
        print("name:", self.__name)
        print("age:", self.__age)


stu1 = Student("Dikshya", 19)

stu1.display()