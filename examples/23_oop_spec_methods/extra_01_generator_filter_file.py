
from pprint import pprint
import re


def filter_file(file_obj, filter_regex):
    for line in file_obj:
        match_line = re.search(filter_regex, line)
        if match_line:
            yield line


if __name__ == "__main__":
    with open("configs/cfg.txt") as f:
        fl = filter_file(f, r"^interface|ip address")
        for line in fl:
            pprint(line)

