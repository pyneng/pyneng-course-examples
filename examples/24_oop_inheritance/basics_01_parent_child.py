from datetime import datetime

class Parent:
    def __init__(self, name):
        print("__init__ Parent")
        self.name = name

    def info(self):
        print("method info parent")
        print(f"Parent {self.name}")


class Child(Parent):
    pass
