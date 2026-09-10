# 💬 Chat System — Python OOP

A simple **Chat System** built using Python Object-Oriented Programming (OOP) concepts.

This project simulates a basic chatroom where users can join or leave a room, send messages, and view chat history.

## 📌 Features

* 👤 Create users
* 💬 Create a chatroom
* 🚪 Join and leave a chatroom
* 📩 Send messages
* 🆔 Automatically assign message IDs
* 📜 View chat history
* 🚫 Prevent users from sending messages when they are not in a chatroom

## 🧠 OOP Concepts Used

This project demonstrates several Python OOP concepts:

| Concept                 | Usage                                                   |
| ----------------------- | ------------------------------------------------------- |
| **Class**               | `User`, `Message`, `ChatRoom`                           |
| **Object**              | Users, chatroom, and messages are created as objects    |
| **Constructor**         | `__init__()` initializes object data                    |
| **Instance Attributes** | `username`, `chatroom`, `content`, `id`                 |
| **Class Variable**      | `message_counter` keeps track of message IDs            |
| **Instance Methods**    | `join_chatroom()`, `leave_chatroom()`, `send_message()` |
| **Magic Method**        | `__str__()` controls message display                    |
| **Object Interaction**  | `User`, `ChatRoom`, and `Message` objects work together |

## 🏗️ Classes

### 1. `Message`

Represents a message sent by a user.

It stores:

* Message ID
* Sender
* Message content

The `message_counter` class variable automatically generates message IDs.

Example:

```text
(1) Alice: Hello everyone!
(2) Bob: Hi Alice!
```

### 2. `User`

Represents a user in the chat system.

Main methods:

```python
join_chatroom()
leave_chatroom()
send_message()
```

A user can only send a message after joining a chatroom.

### 3. `ChatRoom`

Represents the chatroom.

It stores:

* Chatroom name
* List of users
* List of messages

Main methods:

```python
add_user()
remove_user()
broadcast()
show_chat_history()
```

## 🔄 How It Works

```text
Create ChatRoom
      ↓
Create Users
      ↓
User joins ChatRoom
      ↓
User sends Message
      ↓
ChatRoom creates Message object
      ↓
Message is stored
      ↓
View Chat History
      ↓
User leaves ChatRoom
```

## ▶️ Example

```python
room = ChatRoom("Python Lounge")

u1 = User("Alice")
u2 = User("Bob")

u1.join_chatroom(room)
u2.join_chatroom(room)

u1.send_message("Hello everyone!")
u2.send_message("Hi Alice!")

room.show_chat_history()
```

### Example Output

```text
Alice joined Python Lounge
Bob joined Python Lounge

(1) Alice: Hello everyone!
(2) Bob: Hi Alice!

Chat History of Python Lounge:

(1) Alice: Hello everyone!
(2) Bob: Hi Alice!
```

## 📂 Project Structure

```text
MINI_Chat_System/
│
├── code.py
└── README.md
```

## 🎯 Learning Outcome

Through this project, I practiced how multiple Python OOP concepts can work together in a real-world-style application.

The project helped me understand:

* How classes and objects interact
* How constructors initialize objects
* How instance and class variables work
* How methods communicate between objects
* How objects can be stored inside lists
* How magic methods such as `__str__()` can customize object behavior

## 🚀 Future Improvements

Possible improvements for this project:

* Private/protected attributes
* User authentication
* Multiple chatrooms
* Message timestamps
* Delete messages
* Search chat history
* File/image sharing
* Database integration
* Graphical or web-based interface

---

**Built as part of my Python OOP learning journey. 🐍💻**
