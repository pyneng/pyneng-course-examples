item_list = ["1", "2", "test", "3", "4", "line", "5", "6"]

for item in item_list.copy():
    if not item.isdigit():
        item_list.remove(item)
    else:
        print(item)

print(item_list)
