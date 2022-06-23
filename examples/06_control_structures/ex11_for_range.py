from pprint import pprint


vlan_list = ["1", "10", "110", "12", "100"]

# for vlan in vlan_list:
#     print(vlan)
for index in range(len(vlan_list)):
    vlan_list[index] = int(vlan_list[index])
    print("внутри цикла", vlan_list)


# print(f"{vlan=}")
# print(f"vlan={vlan}")
print(vlan_list)
print("The end")
