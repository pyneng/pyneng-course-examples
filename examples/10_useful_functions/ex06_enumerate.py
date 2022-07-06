from pprint import pprint

with open("config_r1.txt") as f:
    for num, line in enumerate(f, 1):
        if line.startswith("interface"):
            print(num, line, end="")
