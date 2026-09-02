fruits = {"apple", "banana", "mango", "orange"}

print(fruits)
print(len(fruits))
print(type(fruits))

#add
fruits.add("litchi")
print(fruits)

#update
fruits.update(["grape", "watermelon"])
print(fruits)

#remove
fruits.remove("banana")
#fruits.remove("guava") gives error

#discard
fruits.discard("guava")
print(fruits)

fruits.pop()
print(fruits)

print("apple" in fruits)
print("banana" in fruits)