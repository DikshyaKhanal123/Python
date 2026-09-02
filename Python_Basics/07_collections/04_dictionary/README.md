# 🐍 Python Dictionaries

A **dictionary** in Python is a collection used to store data in **key-value pairs**.

Unlike lists and tuples, dictionaries allow us to access data using a meaningful **key** instead of a numeric index.

---

## 📌 What is a Dictionary?

A dictionary stores data in the form:

```text
key → value
```

### Example

```python
student = {
    "name": "Dikshya",
    "age": 20,
    "course": "Computer Engineering"
}
```

Here:

* `"name"` → key
* `"Dikshya"` → value
* `"age"` → key
* `20` → value
* `"course"` → key
* `"Computer Engineering"` → value

---

## 🤔 Why Use a Dictionary?

Dictionaries are useful when we want to associate a **meaningful name with a value**.

### Using a list

```python
student = ["Dikshya", 20, "Computer Engineering"]

print(student[1])
```

We need to remember that index `1` represents the age.

### Using a dictionary

```python
student = {
    "name": "Dikshya",
    "age": 20,
    "course": "Computer Engineering"
}

print(student["age"])
```

The dictionary makes the code easier to understand because `"age"` clearly tells us what data we are accessing.

---

## 📝 Creating a Dictionary

A dictionary is created using curly braces `{}`.

```python
student = {
    "name": "Ram",
    "age": 20,
    "roll": 15
}
```

An empty dictionary can be created using:

```python
student = {}
```

---

## 🔑 Accessing Dictionary Values

Values can be accessed using their keys.

```python
student = {
    "name": "Ram",
    "age": 20
}

print(student["name"])
print(student["age"])
```

Output:

```text
Ram
20
```

If the key does not exist, using `[]` produces a `KeyError`.

---

## 🛡️ `get()` Method

The `get()` method is used to access a value safely.

```python
print(student.get("name"))
```

Output:

```text
Ram
```

If the key does not exist:

```python
print(student.get("city"))
```

Output:

```text
None
```

This is safer than:

```python
print(student["city"])
```

because `student["city"]` would produce a `KeyError` if `"city"` does not exist.

---

# ✏️ Adding and Changing Items

Dictionaries are **mutable**, so we can change them after creation.

### Adding a new item

```python
student["city"] = "Kathmandu"
```

### Changing an existing value

```python
student["age"] = 21
```

Example:

```python
student = {
    "name": "Ram",
    "age": 20
}

student["age"] = 21
student["city"] = "Kathmandu"

print(student)
```

Output:

```text
{'name': 'Ram', 'age': 21, 'city': 'Kathmandu'}
```

---

# 🔄 Dictionary is Mutable

A dictionary is **mutable**.

Mutable means that its contents can be changed after the dictionary is created.

```python
student = {
    "name": "Ram",
    "age": 20
}

student["age"] = 21
```

The original dictionary has been modified.

### Quick comparison

| Data Type  | Mutable? |
| ---------- | -------- |
| String     | ❌ No     |
| Tuple      | ❌ No     |
| List       | ✅ Yes    |
| Dictionary | ✅ Yes    |
| Set        | ✅ Yes    |

---

# 🔍 Membership Operators

The `in` operator checks whether a **key** exists in a dictionary.

```python
student = {
    "name": "Ram",
    "age": 20
}

print("name" in student)
print("city" in student)
```

Output:

```text
True
False
```

### `not in`

```python
print("city" not in student)
```

Output:

```text
True
```

> Important: `in` checks **keys**, not values.

---

# 📏 `len()`

The `len()` function returns the number of key-value pairs.

```python
student = {
    "name": "Ram",
    "age": 20,
    "roll": 15
}

print(len(student))
```

Output:

```text
3
```

---

# 🧰 Dictionary Methods

## 1. `keys()`

Returns all keys.

```python
print(student.keys())
```

Example:

```text
dict_keys(['name', 'age', 'roll'])
```

---

## 2. `values()`

Returns all values.

```python
print(student.values())
```

Example:

```text
dict_values(['Ram', 20, 15])
```

---

## 3. `items()`

Returns all key-value pairs.

```python
print(student.items())
```

Example:

```text
dict_items([
    ('name', 'Ram'),
    ('age', 20),
    ('roll', 15)
])
```

This method is especially useful with loops.

---

## 4. `update()`

Used to add new items or update existing items.

### Add an item

```python
student.update({
    "city": "Kathmandu"
})
```

### Update an existing item

```python
student.update({
    "age": 21
})
```

---

## 5. `pop()`

Removes an item using its key.

```python
student.pop("age")
```

It can also return the removed value:

```python
removed = student.pop("age")

print(removed)
```

---

## 6. `popitem()`

Removes and returns the **last inserted key-value pair**.

```python
student.popitem()
```

---

## 7. `clear()`

Removes all items from the dictionary.

```python
student.clear()

print(student)
```

Output:

```text
{}
```

The dictionary still exists, but it is empty.

---

## 8. `copy()`

Creates a copy of the dictionary.

```python
student_copy = student.copy()

print(student_copy)
```

---

## 9. `setdefault()`

Returns the value of a key.

If the key does not exist, it adds the key with a default value.

```python
student = {
    "name": "Ram",
    "age": 20
}

student.setdefault("city", "Kathmandu")

print(student)
```

Output:

```text
{'name': 'Ram', 'age': 20, 'city': 'Kathmandu'}
```

If `"city"` already exists, `setdefault()` does not replace its existing value.

---

## 10. `fromkeys()`

Creates a new dictionary from a collection of keys.

```python
keys = ["name", "age", "city"]

student = dict.fromkeys(keys, "Not Available")

print(student)
```

Output:

```text
{
    'name': 'Not Available',
    'age': 'Not Available',
    'city': 'Not Available'
}
```

---

# 📋 Dictionary Methods Summary

| Method         | Purpose                       |
| -------------- | ----------------------------- |
| `get()`        | Safely access a value         |
| `keys()`       | Get all keys                  |
| `values()`     | Get all values                |
| `items()`      | Get key-value pairs           |
| `update()`     | Add or update items           |
| `pop()`        | Remove an item using its key  |
| `popitem()`    | Remove the last inserted item |
| `clear()`      | Remove all items              |
| `copy()`       | Create a copy                 |
| `setdefault()` | Get a value or add a default  |
| `fromkeys()`   | Create dictionary from keys   |

---

# 🆚 List vs Tuple vs Dictionary

| Feature | List              | Tuple             | Dictionary        |
| ------- | ----------------- | ----------------- | ----------------- |
| Syntax  | `[]`              | `()`              | `{}`              |
| Access  | Index             | Index             | Key               |
| Ordered | ✅                 | ✅                 | ✅                 |
| Mutable | ✅                 | ❌                 | ✅                 |
| Stores  | Items             | Items             | Key-value pairs   |
| Example | `["Ram", "Sita"]` | `("Ram", "Sita")` | `{"name": "Ram"}` |

---

# 🌍 Real-Life Example

A student record can naturally be represented using a dictionary:

```python
student = {
    "name": "Dikshya",
    "age": 20,
    "roll": 15,
    "course": "Computer Engineering",
    "city": "Kathmandu"
}
```

We can easily access individual information:

```python
print(student["name"])
print(student["course"])
print(student["city"])
```

This is one of the main advantages of dictionaries: **data is stored with meaningful labels.**

---

# 🔑 Key Points to Remember

* Dictionary stores data as **key-value pairs**.
* Dictionaries use `{}`.
* Each key should be **unique**.
* Values can be of different data types.
* Dictionaries are **mutable**.
* Values can be accessed using keys.
* `get()` is useful for safe access.
* `keys()` returns keys.
* `values()` returns values.
* `items()` returns key-value pairs.
* `update()` adds or modifies data.
* `pop()` removes an item using its key.
* `clear()` removes all items.
* `in` checks for the existence of a **key**.
* `len()` gives the number of key-value pairs.

---


