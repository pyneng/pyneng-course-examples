# from rich import print as rprint
from rich import print
from pprint import pprint


vlans = ["1", "2", "3", "test", "4", "5", "switchport allowed vlans add", "100", "2000", "switchport mode trunk"]

print(vlans)

vlans_list = []
for vl in vlans:
    if vl.isdigit():
        print(f"inside if", vl)
        pprint(vl)
        new_vl = int(vl)
        vlans_list.append(new_vl)

print(vlans_list)
