from pprint import pprint
import os


try:
    with open('r1_.txt', 'r') as f:
        for line in f:
            pprint(line)
            if "ip" in line:
                break
        print("=" * 10)
except FileNotFoundError:
    print("Такого файла нет")

filename = "r1_.txt"

if os.path.exists(filename):
    with open(filename, 'r') as f:
        for line in f:
            pprint(line)
            if "ip" in line:
                break
        print("=" * 10)
else:
    print("Такого файла нет")
