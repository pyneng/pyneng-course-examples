data = [(2, 200), (3, 300), (4, 400)]

for item1, item2 in data:
    print(item1, item2)


access = {'0/12': 10, '0/14': 11, '0/16': 17}
print(access.items())
for intf in access.keys():
    vlan = access[intf]
    print(intf, vlan)

for intf, vlan in access.items():
    print(intf, vlan)


data = [(1, 2, 200), (1, 3, 300), (1, 4, 400)]

for item1, *items in data:
    print(item1, items)

