from datetime import datetime


class Parent:
    def __init__(self, name):
        print("parent __init__")
        self.name = name

    def info(self):
        print(f"Parent {self.name}")


class Child(Parent):
    def __init__(self, name, count):
        print("Child __init__")
        #Parent.__init__(self, name) # 1
        #super(Child, self).__init__(name) # 2
        super().__init__(name) # 3
        self.count = count

    def date(self):
        print(datetime.now())
