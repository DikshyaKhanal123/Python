# Python Tuples

Today I learned about **Tuples in Python** and practiced different tuple operations.

## What is a Tuple?

A **tuple** is a collection used to store multiple values in a single variable.

A tuple is similar to a list, but the main difference is that a tuple is **immutable**.

```python
student = ("Ram", "Sita", "Hari")
```

Tuples are generally written using **parentheses `()`**.

---

## Why Use Tuples?

Tuples are useful when we have data that should **not be changed**.

For example:

```python
date_of_birth = (15, 5, 2005)
```

Since the values are fixed, a tuple can be used to represent them.

### Simple Difference

```text
List  → data can be changed
Tuple → data cannot be changed
```

---

## 1. Creating a Tuple

### Basic Syntax

```python
tuple_name = (item1, item2, item3)
```

Example:

```python
fruits = ("Apple", "Banana", "Mango")
```

Check the type:

```python
print(type(fruits))
```

Output:

```text
<class 'tuple'>
```

---

## 2. Tuple with Different Data Types

A tuple can contain different types of values.

```python
student = ("Dikshya", 20, 85.5, True)
```

---

## 3. Tuple Indexing

Tuples use indexing just like strings and lists.

Python starts indexing from `0`.

```python
students = ("Ram", "Sita", "Hari")
```

```text
Ram    Sita    Hari
 0      1       2
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

---

## 4. Negative Indexing

Tuples also support negative indexing.

```python
students = ("Ram", "Sita", "Hari")
```

```text
Ram    Sita    Hari
-3     -2      -1
```

Example:

```python
print(students[-1])
```

Output:

```text
Hari
```

---

## 5. Tuple Slicing

Tuples support slicing.

### Syntax

```python
tuple[start:stop:step]
```

Example:

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
```

Output:

```text
(20, 30, 40)
```

### Reverse a Tuple

```python
print(numbers[::-1])
```

Output:

```text
(50, 40, 30, 20, 10)
```

---

## 6. Tuple Immutability

The most important property of a tuple is that it is **immutable**.

This means that once a tuple is created, its elements cannot be changed.

Example:

```python
students = ("Ram", "Sita", "Hari")

students[1] = "Gita"
```

This produces an error because tuple elements cannot be changed.

```text
TypeError: 'tuple' object does not support item assignment
```

Unlike lists:

```python
students = ["Ram", "Sita", "Hari"]

students[1] = "Gita"
```

Lists can be modified, but tuples cannot.

---

## 7. Finding Tuple Length

The `len()` function returns the number of elements.

```python
students = ("Ram", "Sita", "Hari")

print(len(students))
```

Output:

```text
3
```

---

## 8. Membership Operator

The `in` operator checks whether an element exists in a tuple.

```python
students = ("Ram", "Sita", "Hari")

print("Ram" in students)
print("Gita" in students)
```

Output:

```text
True
False
```

The `not in` operator checks whether an element does not exist.

```python
print("Gita" not in students)
```

Output:

```text
True
```

---

## 9. `count()` Method

The `count()` method counts how many times an element occurs.

```python
students = ("Ram", "Sita", "Ram", "Hari")

print(students.count("Ram"))
```

Output:

```text
2
```

---

## 10. `index()` Method

The `index()` method returns the position of an element.

```python
students = ("Ram", "Sita", "Hari")

print(students.index("Sita"))
```

Output:

```text
1
```

---

## 11. Tuple Concatenation

Two tuples can be combined using the `+` operator.

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print(result)
```

Output:

```text
(1, 2, 3, 4, 5, 6)
```

A new tuple is created instead of modifying the existing tuples.

---

## 12. Tuple Repetition

The `*` operator can repeat a tuple.

```python
numbers = (1, 2)

print(numbers * 3)
```

Output:

```text
(1, 2, 1, 2, 1, 2)
```

---

## 13. Looping Through a Tuple

A `for` loop can be used to access each element.

```python
students = ("Ram", "Sita", "Hari")

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

## 14. Tuple Packing

Multiple values can automatically be packed into a tuple.

```python
student = "Ram", 20, "Computer"
```

Python treats this as:

```python
student = ("Ram", 20, "Computer")
```

This is called **tuple packing**.

---

## 15. Tuple Unpacking

Tuple unpacking allows us to assign tuple values to separate variables.

```python
student = ("Ram", 20, "Computer")

name, age, course = student

print(name)
print(age)
print(course)
```

Output:

```text
Ram
20
Computer
```

Here:

```text
name   → Ram
age    → 20
course → Computer
```

---

## 16. Single-Element Tuple

A single-element tuple requires a comma.

This is **not** a tuple:

```python
number = (10)

print(type(number))
```

Output:

```text
<class 'int'>
```

This is a tuple:

```python
number = (10,)

print(type(number))
```

Output:

```text
<class 'tuple'>
```

### Important

```text
(10)  → integer
(10,) → tuple
```

The comma is what makes it a single-element tuple.

---

# List vs Tuple

| Feature         | List | Tuple |
| --------------- | ---- | ----- |
| Syntax          | `[]` | `()`  |
| Mutable         | Yes  | No    |
| Change elements | Yes  | No    |
| `append()`      | Yes  | No    |
| `remove()`      | Yes  | No    |
| `sort()`        | Yes  | No    |
| `count()`       | Yes  | Yes   |
| `index()`       | Yes  | Yes   |
| Indexing        | Yes  | Yes   |
| Slicing         | Yes  | Yes   |
| Looping         | Yes  | Yes   |

### Simple Rule

Use a **list** when your data may change.

Use a **tuple** when your data should remain fixed.

---

# Tuple Operations Practiced

Today I practiced:

* Creating tuples
* Printing tuples
* Checking tuple type
* Tuple indexing
* Negative indexing
* Tuple slicing
* Reversing tuples
* Finding length using `len()`
* Membership using `in`
* `not in`
* `count()`
* `index()`
* Tuple concatenation
* Tuple repetition
* Looping through tuples
* Tuple packing
* Tuple unpacking
* Single-element tuples
* Understanding tuple immutability
* Comparing lists and tuples

---


## Key Takeaway

> **A tuple is an ordered and immutable collection of values.**

The most important concept learned today:

```text
List  → Mutable
Tuple → Immutable
```

## Next Topic

**Sets in Python**
