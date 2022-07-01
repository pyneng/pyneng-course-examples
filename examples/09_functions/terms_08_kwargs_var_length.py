

def sum_arg(**kwargs):
    print(f"{kwargs=}")
    sum_num = 0
    for arg in kwargs.values():
        sum_num += arg
    return sum_num

"""
In [14]: sum_arg(a=10, b=10, c=20, d=30)
kwargs={'a': 10, 'b': 10, 'c': 20, 'd': 30}
Out[14]: 70

In [15]: sum_arg(a=10, b=10)
kwargs={'a': 10, 'b': 10}
Out[15]: 20

In [16]: sum_arg(a=10)
kwargs={'a': 10}
Out[16]: 10

In [17]: sum_arg()
kwargs={}
Out[17]: 0
"""
