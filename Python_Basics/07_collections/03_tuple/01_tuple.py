# Tuple Operations Practice

student = ("Ram", "Sita", "Hari", "Gita", "Ram")

# 1. Print original tuple
print("Original tuple:", student)

# 2. Find length
print("Length:", len(student))

# 3. Access elements
print("First student:", student[0])
print("Last student:", student[-1])

# 4. Access a specific element
print("Third student:", student[2])

# 5. Slicing
print("First three students:", student[:3])
print("Last two students:", student[-2:])

# 6. Reverse tuple using slicing
print("Reverse:", student[::-1])

# 7. Check whether an item exists
print("Is Ram present?", "Ram" in student)
print("Is Nabin present?", "Nabin" in student)

# 8. Check whether an item does not exist
print("Is Nabin not present?", "Nabin" not in student)

# 9. Find the position of an element
print("Position of Sita:", student.index("Sita"))

# 10. Count an element
print("Number of times Ram appears:", student.count("Ram"))

# 11. Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined = tuple1 + tuple2

print("Combined tuple:", combined)

# 12. Repetition
numbers = (1, 2)

print("Repeated tuple:", numbers * 3)

# 13. Loop through tuple
print("Students:")

for name in student:
    print(name)

# 14. Tuple unpacking
person = ("Dikshya", 20, "Python")

name, age, language = person

print("Name:", name)
print("Age:", age)
print("Language:", language)

# 15. Check type
print("Type:", type(student))