class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("name:", self.name)
        print("age:", self.age)

stu1 = Student("Dikshya", 19)
stu2 = Student("Ram", 30)

stu1.display()
stu2.display()