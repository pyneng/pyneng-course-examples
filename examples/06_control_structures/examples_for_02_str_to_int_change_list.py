from pprint import pprint
vlans = ["10", "20", "30", "40", "50"]

index_range = range(len(vlans))

print(vlans)

for index in index_range:
    vlans[index] = int(vlans[index])

print(vlans)
