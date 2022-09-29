from pprint import pprint

items = ["10", "20", "10", "mode", "1", "11", "20", "trunk"]

vlans = set()
for vl in items:
    if vl.isdigit():
        vlans.add(int(vl))

pprint(vlans)

# set comp

vlans = {int(vl) for vl in items if vl.isdigit()}
pprint(vlans)
