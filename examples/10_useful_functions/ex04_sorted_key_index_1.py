from pprint import pprint
list_of_tuples = [
    ("IT_VLAN", 320),
    ("Mngmt_VLAN", 99),
    ("User_VLAN", 1010),
    ("DB_VLAN", 11),
]

def item_1(item):
    return item[1]

pprint(sorted(list_of_tuples, key=item_1))
pprint(sorted(list_of_tuples, key=lambda x: x[1]))

# change data
new_list = [(item1, item0) for item0, item1 in list_of_tuples]

new_list = []
for item0, item1 in list_of_tuples:
    new_list.append((item1, item0))

pprint(sorted(new_list))
