from pprint import pprint
vlans = ["1", "2", "3", "test", "4", "5", "switchport allowed vlans add", "100", "2000", "switchport mode trunk"]


pprint(vlans)

vlans_list = []
for vl in vlans:
    if vl.isdigit():
        print(f"inside if {vl=}") # python >= 3.8
        # print(f"inside if vl={vl}") # python < 3.8
        new_vl = int(vl)
        print(f"inside if {new_vl=}") # python >= 3.8
        vlans_list.append(new_vl)

print(vlans_list)
