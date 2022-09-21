item_list = ["1", "2", "test", "3", "4", "line", "5", "6"]
vlans = []

for item in item_list:
    if item.isdigit():
        vlans.append(int(item))
    else:
        item_list.remove(item)
print(vlans)
