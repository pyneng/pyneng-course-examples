

vlans = ["1", "2", "3", "test", "4", "5", "switchport allowed vlans add", "100", "2000", "switchport mode trunk"]

from rich import inspect

inspect(vlans)

vlans_list = []
for vl in vlans:
    if vl.isdigit():
        print("="*40)
        inspect(vl)
        new_vl = int(vl)
        vlans_list.append(new_vl)

print(vlans_list)
