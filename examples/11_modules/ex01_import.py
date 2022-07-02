"""
В этом модуле...
"""
from pprint import pprint

a = 10
vlans = [1, 2, 3]


def my_sum(a, b):
    pprint(f"{a}, {b}")
    return a + b


def main():
    print("Start".center(50, "="))
    my_sum(1, 2)
    pprint(vlans)
    print("End".center(50, "="))


# if module called directly:
if __name__ == "__main__":
    main()
