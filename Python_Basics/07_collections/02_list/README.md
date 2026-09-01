# Python Lists

## What is a List?

A **list** is a collection used to store multiple values in a single variable.

```python
students = ["Ram", "Shyam", "Sita", "Gita", "Hari"]
```

Lists are created using **square brackets `[]`**.

---

## 1. Creating a List

```python
fruits = ["Apple", "Banana", "Mango"]
numbers = [10, 20, 30, 40]
```

A list can also contain different data types:

```python
data = ["Dikshya", 20, 85.5, True]
```

---

## 2. Printing a List

```python
students = ["Ram", "Sita", "Hari"]

print(students)
```

Output:

```text
['Ram', 'Sita', 'Hari']
```

---

## 3. Finding Length of a List

The `len()` function returns the number of elements in a list.

```python
print(len(students))
```

Output:

```text
3
```

---

## 4. List Indexing

Each element in a list has an index.

Python starts indexing from `0`.

```text
['Ram', 'Sita', 'Hari']
    0       1       2
```

Example:

```python
print(students[0])
print(students[2])
```

Output:

```text
Ram
Hari
```

### Negative Indexing

Negative indexes access elements from the end.

```python
print(students[-1])
```

Output:

```text
Hari
```

---

## 5. Changing an Element

Lists are **mutable**, which means their elements can be changed after the list is created.

```python
students = ["Ram", "Sita", "Hari"]

students[1] = "Gita"

print(students)
```

Output:

```text
['Ram', 'Gita', 'Hari']
```

---

## 6. Adding an Element with `append()`

`append()` adds one element to the **end** of the list.

```python
students = ["Ram", "Sita"]

students.append("Hari")

print(students)
```

Output:

```text
['Ram', 'Sita', 'Hari']
```

---

## 7. Adding an Element with `insert()`

`insert()` adds an element at a specific position.

### Syntax

```python
list.insert(index, value)
```

Example:

```python
students = ["Ram", "Sita", "Hari"]

students.insert(1, "Gita")

print(students)
```

Output:

```text
['Ram', 'Gita', 'Sita', 'Hari']
```

---

## 8. Adding Multiple Elements with `extend()`

`extend()` adds multiple elements from another iterable, commonly another list.

```python
students = ["Ram", "Sita"]

students.extend(["Hari", "Gita"])

print(students)
```

Output:

```text
['Ram', 'Sita', 'Hari', 'Gita']
```

### `append()` vs `extend()`

```python
students.append(["Hari", "Gita"])
```

adds the entire list as **one element**.

```python
students.extend(["Hari", "Gita"])
```

adds `"Hari"` and `"Gita"` as separate elements.

---

## 9. Checking Whether an Element Exists

The `in` operator checks whether an element is present in a list.

```python
students = ["Ram", "Sita", "Hari"]

print("Ram" in students)
print("Gita" in students)
```

Output:

```text
True
False
```

---

## 10. Removing an Element with `remove()`

`remove()` removes an element using its **value**.

```python
students = ["Ram", "Sita", "Hari"]

students.remove("Sita")

print(students)
```

Output:

```text
['Ram', 'Hari']
```

---

## 11. Removing an Element with `pop()`

`pop()` removes an element using its **index**.

```python
students = ["Ram", "Sita", "Hari"]

students.pop(1)

print(students)
```

Output:

```text
['Ram', 'Hari']
```

### `pop()` without an index

If no index is provided, `pop()` removes the last element.

```python
students.pop()
```

---

## 12. `remove()` vs `pop()`

This is an important difference:

```text
remove() → removes by VALUE
pop()    → removes by INDEX
```

Example:

```python
students.remove("Hari")
```

removes `"Hari"`.

```python
students.pop(2)
```

removes whatever element is at index `2`.

---

## 13. Counting Elements with `count()`

`count()` tells how many times an element occurs in a list.

```python
students = ["Ram", "Gita", "Ram", "Hari"]

print(students.count("Ram"))
```

Output:

```text
2
```

---

## 14. Finding an Element with `index()`

`index()` returns the index of an element.

```python
students = ["Ram", "Sita", "Hari"]

print(students.index("Hari"))
```

Output:

```text
2
```

---

## 15. Sorting a List

The `sort()` method arranges the elements in ascending order.

```python
students = ["Ram", "Shyam", "Sita", "Gita", "Hari"]

students.sort()

print(students)
```

Output:

```text
['Gita', 'Hari', 'Ram', 'Shyam', 'Sita']
```

Names can also be sorted because they are strings.

### Descending order

```python
students.sort(reverse=True)

print(students)
```

---

## 16. Important `sort()` Concept

`sort()` changes the original list and returns `None`.

Therefore, this is not the correct way to print the sorted list:

```python
print(students.sort())
```

It produces:

```text
None
```

Instead:

```python
students.sort()
print(students)
```

---

## 17. Reversing a List

The `reverse()` method reverses the order of elements.

```python
numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)
```

Output:

```text
[40, 30, 20, 10]
```

---

## 18. List Slicing

Lists support slicing.

### Syntax

```python
list[start:stop:step]
```

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

### Reverse using slicing

```python
print(numbers[::-1])
```

Output:

```text
[50, 40, 30, 20, 10]
```

---

## 19. List Concatenation

The `+` operator can combine two lists.

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2

print(result)
```

Output:

```text
[1, 2, 3, 4, 5, 6]
```

---

## 20. List Repetition

The `*` operator can repeat a list.

```python
numbers = [1, 2]

print(numbers * 3)
```

Output:

```text
[1, 2, 1, 2, 1, 2]
```

---

## 21. Looping Through a List

A `for` loop can be used to access every element.

```python
students = ["Ram", "Sita", "Hari"]

for student in students:
    print(student)
```

Output:

```text
Ram
Sita
Hari
```

---

## 22. Copying a List

The `copy()` method creates a copy of a list.

```python
students = ["Ram", "Sita", "Hari"]

new_students = students.copy()

print(new_students)
```

---

## 23. Clearing a List

`clear()` removes all elements from a list.

```python
students = ["Ram", "Sita", "Hari"]

students.clear()

print(students)
```

Output:

```text
[]
```

---

# List Operations Summary

| Operation             | Purpose                               |
| --------------------- | ------------------------------------- |
| `len()`               | Find number of elements               |
| `list[index]`         | Access an element                     |
| `list[index] = value` | Change an element                     |
| `append()`            | Add one element at the end            |
| `insert()`            | Add an element at a specific position |
| `extend()`            | Add multiple elements                 |
| `remove()`            | Remove by value                       |
| `pop()`               | Remove by index                       |
| `count()`             | Count occurrences                     |
| `index()`             | Find the position                     |
| `sort()`              | Sort the list                         |
| `reverse()`           | Reverse the list                      |
| `copy()`              | Copy the list                         |
| `clear()`             | Remove all elements                   |
| `in`                  | Check membership                      |
| `+`                   | Combine lists                         |
| `*`                   | Repeat lists                          |
| `[:]`                 | Slice a list                          |

---

# Important Concepts Learned

### Lists are Mutable

Unlike strings, lists can be changed after creation.

```python
students[0] = "Dikshya"
```

### `remove()` vs `pop()`

```text
remove() → value
pop()    → index
```

### `append()` vs `extend()`

```text
append() → adds one item
extend() → adds multiple items
```

### `sort()` vs `sorted()`

```text
sort()    → changes the original list
sorted()  → creates a new sorted list
```

---


## Next Topic

**Tuples in Python**
