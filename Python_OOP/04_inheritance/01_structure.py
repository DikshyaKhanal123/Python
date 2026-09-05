class Parent:

    def parent_method(self):
        print("This is parent")


class Child(Parent):

    def child_method(self):
        print("This is child")


obj = Child()

obj.parent_method()
obj.child_method()