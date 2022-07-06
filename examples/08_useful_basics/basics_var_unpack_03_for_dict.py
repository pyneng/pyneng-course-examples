from pprint import pprint


access = {"0/12": 10, "0/14": 11, "0/16": 17}
# access.items()
# dict_items([('0/12', 10), ('0/14', 11), ('0/16', 17)])

for intf, vlan in access.items():
    print(intf, vlan)
