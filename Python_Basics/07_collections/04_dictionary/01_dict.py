student = {
    "name": "Dikshya",
    "age": 20,
    "roll": 15,
    "course": "Computer Engineering"
}

print(student)
print(len(student))
print(type(student))

#accessing value using keys
print("name:", student["name"])

#get
print(student.get("name"))
print(student.get("age"))

#adding a new item 
student["city"] = "ktm"
print(student)

#chnaging an existing value
student["age"] = 15
print(student)

#keys
print(student.keys())

#values
print(student.values())

#items
print(student.items())


#update
student.update({
    "email" : "dikshya12@gmail.com",
    "age" : 50
})
print(student)

#checking key using in
print("name " in student)

#pop
student.pop("email")
print(student)