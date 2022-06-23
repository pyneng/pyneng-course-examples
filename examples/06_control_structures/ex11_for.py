from pprint import pprint


vlan_list = ["1", "10", "110", "12", "100"]

vlan_int_list = []

# для каждого влана в списке vlan_list
for vlan in vlan_list:
    vlan_int = int(vlan)
    vlan_int_list.append(vlan_int)
    print("внутри цикла", vlan_int_list)


# print(f"{vlan=}")
# print(f"vlan={vlan}")
print(vlan_list)
print(vlan_int_list)
print("The end")
