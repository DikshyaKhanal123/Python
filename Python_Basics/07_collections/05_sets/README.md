# 🐍 Python Sets

A **set** is a built-in collection data type in Python used to store **unique elements**.

Sets are especially useful when we need to remove duplicate values, perform membership checking, or perform mathematical operations such as union, intersection, and difference.

---

## 📌 What is a Set?

A set is a collection of unique elements.

```python
numbers = {10, 20, 30, 40}
```

A set does not allow duplicate values.

```python
numbers = {10, 20, 20, 30, 30}

print(numbers)
```

Output:

```text
{10, 20, 30}
```

The duplicate values are automatically removed.

---

## 🤔 Why Use Sets?

Sets are useful when:

* We need only **unique values**.
* We want to **remove duplicates**.
* We need fast **membership checking**.
* We want to compare two groups of data.
* We need operations such as **union, intersection, and difference**.

### Example: Removing Duplicates

```python
numbers = [10, 20, 20, 30, 30, 40]

unique_numbers = set(numbers)

print(unique_numbers)
```

Output:

```text
{10, 20, 30, 40}
```

---

# 📝 Creating a Set

A set can be created using curly braces `{}`.

```python
fruits = {"apple", "banana", "mango"}

print(fruits)
```

---

## ⚠️ Creating an Empty Set

This creates an empty **dictionary**:

```python
empty = {}
```

To create an empty set, use:

```python
empty = set()
```

---

# 🔄 Set is Mutable

A set is **mutable**, which means its elements can be added or removed after the set is created.

```python
numbers = {10, 20, 30}

numbers.add(40)

print(numbers)
```

---

# 🚫 Sets Do Not Allow Duplicate Values

```python
students = {"Ram", "Sita", "Ram", "Hari"}

print(students)
```

The duplicate `"Ram"` is automatically removed.

---

# 🔢 Sets Do Not Support Indexing

Sets are not accessed using indexes like lists and tuples.

```python
numbers = {10, 20, 30}

# numbers[0]  # ❌ TypeError
```

If you need to access elements one by one, you can use a loop:

```python
for number in numbers:
    print(number)
```

---

# 🧰 Set Methods

## 1. `add()`

Adds one element to a set.

```python
numbers = {10, 20, 30}

numbers.add(40)

print(numbers)
```

---

## 2. `update()`

Adds multiple elements to a set.

```python
numbers = {10, 20, 30}

numbers.update([40, 50, 60])

print(numbers)
```

---

## 3. `remove()`

Removes a specific element.

```python
numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)
```

If the element does not exist, `remove()` raises a `KeyError`.

---

## 4. `discard()`

Removes an element without producing an error if the element does not exist.

```python
numbers = {10, 20, 30}

numbers.discard(20)
numbers.discard(50)

print(numbers)
```

### `remove()` vs `discard()`

```text
remove()   → Error if element doesn't exist
discard()  → No error if element doesn't exist
```

---

## 5. `pop()`

Removes and returns an arbitrary element.

```python
numbers = {10, 20, 30, 40}

removed = numbers.pop()

print("Removed:", removed)
print("Remaining:", numbers)
```

Because sets are unordered, we should not assume which element `pop()` will remove.

---

## 6. `clear()`

Removes all elements from a set.

```python
numbers = {10, 20, 30}

numbers.clear()

print(numbers)
```

Output:

```text
set()
```

---

## 7. `copy()`

Creates a copy of a set.

```python
numbers = {10, 20, 30}

numbers_copy = numbers.copy()

print(numbers_copy)
```

---

# 🔥 Set Operations

Set operations are useful for comparing groups of data.

```python
python_students = {"Ram", "Sita", "Hari"}
java_students = {"Sita", "Hari", "Gita"}
```

---

## 8. `union()`

Returns all unique elements from both sets.

```python
result = python_students.union(java_students)

print(result)
```

Concept:

```text
Python → Ram, Sita, Hari
Java   → Sita, Hari, Gita

Union  → Ram, Sita, Hari, Gita
```

The `|` operator can also be used:

```python
result = python_students | java_students
```

---

## 9. `intersection()`

Returns elements that exist in both sets.

```python
result = python_students.intersection(java_students)

print(result)
```

Output:

```text
{'Sita', 'Hari'}
```

The `&` operator can also be used:

```python
result = python_students & java_students
```

---

## 10. `difference()`

Returns elements that exist in the first set but not in the second set.

```python
result = python_students.difference(java_students)

print(result)
```

Output:

```text
{'Ram'}
```

The `-` operator can also be used:

```python
result = python_students - java_students
```

---

## 11. `symmetric_difference()`

Returns elements that exist in either set but **not in both**.

```python
result = python_students.symmetric_difference(java_students)

print(result)
```

Result:

```text
{'Ram', 'Gita'}
```

The `^` operator can also be used:

```python
result = python_students ^ java_students
```

---

# 🔍 Set Checking Methods

## 12. `issubset()`

Checks whether all elements of one set exist in another set.

```python
all_students = {"Ram", "Sita", "Hari", "Gita"}
python_students = {"Ram", "Sita"}

print(python_students.issubset(all_students))
```

Output:

```text
True
```

---

## 13. `issuperset()`

Checks whether a set contains all elements of another set.

```python
all_students = {"Ram", "Sita", "Hari", "Gita"}
python_students = {"Ram", "Sita"}

print(all_students.issuperset(python_students))
```

Output:

```text
True
```

---

## 14. `isdisjoint()`

Checks whether two sets have no common elements.

```python
group_a = {"Ram", "Sita"}
group_b = {"Hari", "Gita"}

print(group_a.isdisjoint(group_b))
```

Output:

```text
True
```

If they have a common element:

```python
group_b = {"Hari", "Sita"}

print(group_a.isdisjoint(group_b))
```

Output:

```text
False
```

---

# 🔄 Update Set Operations

These methods modify the original set.

## 15. `intersection_update()`

Keeps only common elements.

```python
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

a.intersection_update(b)

print(a)
```

Output:

```text
{30, 40}
```

---

## 16. `difference_update()`

Removes elements that are also present in another set.

```python
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

a.difference_update(b)

print(a)
```

Output:

```text
{10, 20}
```

---

## 17. `symmetric_difference_update()`

Keeps elements that are not common between the two sets.

```python
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

a.symmetric_difference_update(b)

print(a)
```

Output:

```text
{10, 20, 50, 60}
```

---

# 📏 `len()`

`len()` is a built-in function, not a set method.

It returns the number of elements.

```python
numbers = {10, 20, 30, 40}

print(len(numbers))
```

Output:

```text
4
```

---

# 🔎 Membership Checking

The `in` operator checks whether an element exists in a set.

```python
numbers = {10, 20, 30}

print(20 in numbers)
print(50 in numbers)
```

Output:

```text
True
False
```

---

# 📋 Set Methods Summary

| Method                          | Purpose                                    |
| ------------------------------- | ------------------------------------------ |
| `add()`                         | Add one element                            |
| `update()`                      | Add multiple elements                      |
| `remove()`                      | Remove an element                          |
| `discard()`                     | Remove safely                              |
| `pop()`                         | Remove an arbitrary element                |
| `clear()`                       | Remove all elements                        |
| `copy()`                        | Create a copy                              |
| `union()`                       | Combine two sets                           |
| `intersection()`                | Find common elements                       |
| `difference()`                  | Find elements only in first set            |
| `symmetric_difference()`        | Find non-common elements                   |
| `issubset()`                    | Check subset                               |
| `issuperset()`                  | Check superset                             |
| `isdisjoint()`                  | Check whether sets have no common elements |
| `intersection_update()`         | Keep common elements                       |
| `difference_update()`           | Remove common elements                     |
| `symmetric_difference_update()` | Keep non-common elements                   |

---

# 🆚 List vs Tuple vs Set vs Dictionary

| Feature      | List               | Tuple            | Set           | Dictionary     |
| ------------ | ------------------ | ---------------- | ------------- | -------------- |
| Syntax       | `[]`               | `()`             | `{}`          | `{key: value}` |
| Mutable      | ✅                  | ❌                | ✅             | ✅              |
| Duplicates   | ✅                  | ✅                | ❌             | Keys ❌         |
| Indexing     | ✅                  | ✅                | ❌             | Key-based      |
| Main purpose | Ordered collection | Fixed collection | Unique values | Key-value data |

---

# 🌍 Real-Life Example

Suppose two groups of students are learning programming languages:

```python
python_students = {
    "Ram",
    "Sita",
    "Hari",
    "Gita"
}

java_students = {
    "Sita",
    "Hari",
    "Rita"
}
```

We can easily find:

### Students learning both

```python
python_students.intersection(java_students)
```

### Students learning only Python

```python
python_students.difference(java_students)
```

### All students

```python
python_students.union(java_students)
```

This makes sets very useful for handling **groups of unique data**.

---



# 🔑 Key Takeaways

* A **set stores unique elements**.
* Sets are **mutable**.
* Sets do not support **indexing or slicing**.
* Duplicate elements are automatically removed.
* Use `set()` to create an empty set.
* `add()` adds one element.
* `update()` adds multiple elements.
* `remove()` and `discard()` remove elements.
* `union()` combines sets.
* `intersection()` finds common elements.
* `difference()` finds elements unique to one set.
* `symmetric_difference()` finds non-common elements.
* `issubset()`, `issuperset()`, and `isdisjoint()` are useful for comparing sets.
* Sets are very useful for **removing duplicates and comparing groups of data**.
