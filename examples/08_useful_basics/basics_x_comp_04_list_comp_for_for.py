vlans = [[10, 21, 35], [101, 115, 150], [111, 40, 50]]

result = []

for vl_list in vlans:
    for vl in vl_list:
        result.append(vl)

print(result)

# list comp

result = [vl for vl_list in vlans for vl in vl_list]
print(result)
