from pprint import pprint


items = [10, 20, 30, 1, 1, 11, 100, 1]

# [expression for item in items]
# [expression for item in items if condition]
# [exp1 if cond else exp2 for item in items]

vlans = [vl if vl != 1 else 1111 for vl in items]
pprint(vlans)
