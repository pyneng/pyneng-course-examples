

class PrintLine:
    def __init__(self, line, count=50):
        print("__init__")
        self.line = line
        self.count = count

    def __enter__(self):
        print("__enter__")
        print(self.line * self.count)

    def __exit__(self, exc_type, exc_value, traceback):
        print("__exit__", exc_type, exc_value, traceback)
        print(self.line * self.count)


# pl = PrintLine("*")
# print("=====")
# with pl:
#     print(f"TEST")


with PrintLine("*"):
    print(f"{pl=}")
    print(f"TEST")
