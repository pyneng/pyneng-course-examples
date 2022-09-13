from pprint import pprint

with open("configs/cfg1.txt") as f:
    for index, line in enumerate(f, 1):
        if line.startswith("interface"):
            print(f"{index:3} {line}")
