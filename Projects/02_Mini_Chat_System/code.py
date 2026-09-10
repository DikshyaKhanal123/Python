# Message class

class Message:
    message_counter = 1

    def __init__(self, sender, content):
        self.sender = sender
        self. content = content
        self.id = Message.message_counter
        Message.message_counter += 1

    def __str__(self):
        return f"({self.id}) {self.sender.username}:{self.content}"


# User Class

class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

    def join_chatroom(self,chatroom):
        if self.chatroom:
            print(f"{self.username} is already in a chatroom.")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} joined {chatroom.name}")

    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in the chatroom")
        else:
            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.name}")
            self.chatroom = None

    def send_message(self,content):
        if not self.chatroom:
            print(f"{self.username} cannot send a message (not in a chatroom).")
        else:
            self.chatroom.broadcast(self,content)

# chatroom class

class ChatRoom:
    def __init__(self,name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self,user):
        self.users.append(user)

    def remove_user(self,user):
        self.users.remove(user)

    def broadcast(self, sender, content):
        message = Message(sender, content)
        self.messages.append(message)
        print(message) #show messages to all users

    def show_chat_history(self):
        print(f" \n Chat History of {self.name}")
        for msg in self.messages:
            print(msg)

#example usage

if __name__ == "__main__":
    room = ChatRoom("python")

    u1= User("Alice")
    u2 = User ("BOb")
    u3 = User("charlie")

    u1.join_chatroom(room)
    u2.join_chatroom(room)

    u1.send_message("hello")
    u2.send_message("hii")

    u3.join_chatroom(room)
    u3.send_message("hey guys")

    room.show_chat_history()

    u1.leave_chatroom()
    u2.leave_chatroom()
    u3.leave_chatroom()
