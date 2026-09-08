class Student:
    def __init__(self,name,age,gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def display(self):
        print("name:", self.name)
        print("age:", self.age)
        print("gpa:" ,self.gpa)

stu1 = Student("Dikshya", 19.3.2)
stu2 = Student("Ram", 30.4.0)

stu1.display()
stu2.display()