class Parent:
    def display(self):
        print("this is parent")

class Child(Parent):
    def show(self):
        print("this is child")

c = Child()
c.show()