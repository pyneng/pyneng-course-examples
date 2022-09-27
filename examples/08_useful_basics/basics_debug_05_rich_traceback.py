# from rich.traceback import install
# install(show_locals=True)


vlans = ["1", "2", "3", "test", "4", "5", "switchport allowed vlans add", "100", "2000", "switchport mode trunk"]


vlans_list = []
for vl in vlans:
    # if vl.isdigit():
    new_vl = int(vl)
    vlans_list.append(new_vl)

print(vlans_list)
