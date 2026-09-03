class Student:
    subject = "python"
    college = "abc"
    year = "4th year"

stu1 = Student()
stu2 = Student()
print(stu1.subject)
print(stu1.year)
print(stu2.subject)
print(stu2.college)


#accessing class attribute using class itself
print(Student.college)
print(Student.year)