"""
В этом модуле...
"""
from pprint import pprint
from sys import version, argv
import concurrent.futures as cf

x = 10
vlans = [1, 2, 3]


def my_sum(a, b):
    return a + b


if __name__ == "__main__":
    result = my_sum(1, 2)

    print("start".center(50, "="))
    print(version)
    print("end".center(50, "="))
