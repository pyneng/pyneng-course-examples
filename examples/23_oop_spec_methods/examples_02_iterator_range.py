

class MyRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.last_value = start

    def __next__(self):
        print("__next__")
        value = self.last_value
        if self.last_value == self.stop:
            raise StopIteration
        self.last_value += 1
        return value

    def __iter__(self):
        print("__iter__")
        return self
