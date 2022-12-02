from pprint import pprint
import re


class FilterFile:
    def __init__(self, file_obj, filter_regex):
        self.file_obj = file_obj
        self.filter_regex = filter_regex

    def __next__(self):
        print("__next__")
        while True:
            line = next(self.file_obj)
            print(f">>>> {line=}")
            match_line = re.search(self.filter_regex, line)
            if match_line:
                return line

    def __iter__(self):
        return self


if __name__ == "__main__":
    with open("configs/cfg.txt") as f:
        fl = FilterFile(f, r"^interface|ip address")
        for line in fl:
            pprint(line)
