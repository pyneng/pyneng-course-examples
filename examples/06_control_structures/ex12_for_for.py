vlans = [1, 2, 3, 4, 5]
access_template = [
    "switchport mode access",
    "spanning-tree bpduguard enable",
    "cmd3",
    "cmd4",
]

for vl in vlans:
    print(f"switchport access vlan {vl}")
    for cmd in access_template:
        print(cmd)
    print()
