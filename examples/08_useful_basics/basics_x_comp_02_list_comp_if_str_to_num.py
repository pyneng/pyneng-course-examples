from pprint import pprint

items = ["10", "20", "30", "mode", "1", "11", "100", "trunk"]

vlans = []
for vl in items:
    if vl.isdigit():
        vlans.append(int(vl))

pprint(vlans)

# list comp

vlans = [int(vl) for vl in items if vl.isdigit()]
pprint(vlans)
