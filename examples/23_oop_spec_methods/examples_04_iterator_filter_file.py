from pprint import pprint
import re


class FilterFile:
    def __init__(self, file_object, filter_regex):
        self.file_object = file_object
        self.filter_regex = filter_regex

    def __next__(self):
        print("__next__")
        for line in self.file_object:
            match_line = re.search(self.filter_regex, line)
            if match_line:
                return line
        raise StopIteration

    def __iter__(self):
        print("__iter__")
        return self


if __name__ == "__main__":
    with open("configs/cfg.txt") as f:
        fl = FilterFile(f, r"^interface|ip address")
        for line in fl:
            pprint(line)
