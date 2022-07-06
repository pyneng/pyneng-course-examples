from pprint import pprint

items = ["10", "20", "30", "1", "11", "100"]
vlans = []
for vl in items:
    vlans.append(int(vl))

pprint(vlans)

# list comp

vlans = [int(vl) for vl in items]
pprint(vlans)
