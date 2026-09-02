student = {
    "name": "Dikshya",
    "age": 20,
    "roll": 15,
    "course": "Computer Engineering"
}

#loop through keys
for key in student:
    print(key)

#loop through value
for value in student.values():
    print(value)

#loop through item
for key, value in student.items():
    print(key , ":" , value)