students = ["Ram" ,"Shyam" ,"Sita" , "Gita" , "Hari"]

#print original list
print(students)

#print length of list
print(len(students))

#acces elements
print("first student:", students[0])
print("last student:", students[-1])

#change an element
students[3] = "Dikshya"
print(students)

#append element
students.append("Gita")
print(students)

#add  item at specific positon
students.insert(2, "Nita")
print(students)

#check whether item pressent in list
print("ramit" in students)
print("Dikshya" in students)

#remove an item by value
students.remove("Hari")
students.pop(2)
print(students)

#sorting
students.sort()
print(students)

#concatenation of list

teachers = ["Anil" , "Rabi", "Mamata"]
combined = students + teachers
print(combined)

#list repetition
print(teachers *3)

#copy a list

teacher_copy = teachers.copy()
print(teacher_copy)

#count an item
print("number of times Dikshya apprears:", students.count("Dikshya"))