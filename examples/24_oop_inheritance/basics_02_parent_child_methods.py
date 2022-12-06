from datetime import datetime

class Parent:
    def __init__(self, name):
        print("__init__ Parent")
        self.name = name

    def info(self):
        print("method info parent")
        print(f"Parent {self.name}")

    def method(self):
        print("method parent")


class Child(Parent):
    def date(self):
        print("child method date")
        print(f"{datetime.now()}")
        self.method()

    def info(self):
        print("method info child")
        print(f"Child {self.name}")
        # Parent.info(self)
        # super(Child, self).info()
        super().info()
