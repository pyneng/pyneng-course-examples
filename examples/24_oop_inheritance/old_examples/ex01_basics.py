from datetime import datetime

class Parent2:
    pass


class Parent(Parent2):
    def __init__(self, name):
        print("parent __init__")
        self.name = name

    def info(self):
        print(f"parent {self.name}")


class Child(Parent):
    def __init__(self, name, count):
        print("child __init__")
        # Parent.__init__(self, name)
        # super(Child, self).__init__(name)
        super().__init__(name)
        self.count = count

    def date(self):
        self.info()
        print(datetime.now())

    def print(self):
        print("child print")
