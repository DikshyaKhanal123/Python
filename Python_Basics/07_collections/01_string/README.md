# Python Strings

Today I learned about **strings in Python** and practiced different operations that can be performed on strings.

## What is a String?

A string is a sequence of characters used to store text in Python.

```python
name = "Dikshya"
message = 'Hello Python'
```

Strings can contain letters, numbers, spaces, and special characters.

---

## String Indexing

Each character in a string has an index. Python starts indexing from `0`.

```python
word = "Python"

print(word[0])   # P
print(word[2])   # t
print(word[-1])  # n
```

### Index positions

```text
 P   y   t   h   o   n
 0   1   2   3   4   5
-6  -5  -4  -3  -2  -1
```

---

## String Slicing

Slicing is used to extract a part of a string.

### Syntax

```python
string[start:stop:step]
```

Example:

```python
word = "Python"

print(word[0:3])   # Pyt
print(word[::2])   # Pto
print(word[::-1])  # nohtyP
```

---

## String Operations

### 1. Concatenation

The `+` operator joins strings.

```python
first_name = "Dikshya"
last_name = "Khanal"

full_name = first_name + " " + last_name

print(full_name)
```

Output:

```text
Dikshya Khanal
```

### 2. Repetition

The `*` operator repeats a string.

```python
print("Hello " * 3)
```

Output:

```text
Hello Hello Hello
```

### 3. Length

`len()` returns the number of characters.

```python
word = "Python"

print(len(word))
```

Output:

```text
6
```

### 4. Membership

`in` checks whether something exists inside a string.

```python
word = "Python"

print("Python" in word)
print("Java" in word)
```

Output:

```text
True
False
```

---

## String Methods

I practiced the following methods:

| Method         | Purpose                                       |
| -------------- | --------------------------------------------- |
| `upper()`      | Converts text to uppercase                    |
| `lower()`      | Converts text to lowercase                    |
| `capitalize()` | Capitalizes the first character               |
| `title()`      | Capitalizes each word                         |
| `strip()`      | Removes spaces from both sides                |
| `lstrip()`     | Removes spaces from the left                  |
| `rstrip()`     | Removes spaces from the right                 |
| `replace()`    | Replaces text                                 |
| `find()`       | Finds the position of text                    |
| `count()`      | Counts occurrences                            |
| `split()`      | Splits a string into a list                   |
| `join()`       | Joins items into a string                     |
| `startswith()` | Checks the beginning                          |
| `endswith()`   | Checks the ending                             |
| `isalpha()`    | Checks whether characters are alphabetic      |
| `isdigit()`    | Checks whether characters are digits          |
| `isalnum()`    | Checks whether characters are letters/numbers |
| `islower()`    | Checks whether text is lowercase              |
| `isupper()`    | Checks whether text is uppercase              |

---

## Example

```python
word = "I love Python"

print(f"Original string: {word}")
print(f"Length: {len(word)}")
print(f"First character: {word[0]}")
print(f"Reverse: {word[::-1]}")
print(f"Uppercase: {word.upper()}")
print(f"Lowercase: {word.lower()}")
print(f"Split: {word.split()}")
print(f"Position of love: {word.find('love')}")
print(f"Python in string: {'Python' in word}")
```

---

## Split and Join

### `split()`

`split()` converts a string into a list.

```python
text = "Python is easy"

words = text.split()

print(words)
```

Output:

```text
['Python', 'is', 'easy']
```

### `join()`

`join()` combines multiple strings into one string.

```python
words = ["Python", "is", "easy"]

sentence = " ".join(words)

print(sentence)
```

Output:

```text
Python is easy
```

---

## F-Strings

I also practiced **f-strings**, which make it easy to combine variables and text.

```python
name = "Dikshya"
age = 20

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Dikshya and I am 20 years old.
```

---

## Escape Characters

I practiced special characters such as:

```python
print("Hello\nPython")
print("Name:\tDikshya")
```

* `\n` → New line
* `\t` → Tab

---

## Important Concept: Strings are Immutable

Strings cannot be directly changed after they are created.

```python
word = "Python"

# word[0] = "J"   # Error
```

Instead, a new string is created:

```python
word = "Jython"
```

---

## Practice

Today I practiced:

* Creating strings
* String indexing
* Negative indexing
* String slicing
* Reversing strings
* String concatenation
* String repetition
* Finding string length
* Membership operators
* Changing string case
* Removing spaces
* Replacing text
* Finding text
* Counting characters
* Splitting strings
* Joining strings
* Checking string properties
* Escape characters
* F-strings

## Next Topic

**Python Collections**

* Lists
* Tuples
* Sets
* Dictionaries
