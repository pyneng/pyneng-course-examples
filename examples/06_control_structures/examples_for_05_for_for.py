commands = [
    "switchport mode access",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]
intf_list = ["0/1", "0/3", "0/4", "0/11"]

for intf in intf_list:
    print(f"interface FastEthernet{intf}")
    for cmd in commands:
        print(f" {cmd}")


"""
interface FastEthernet0/1
 switchport mode access
 spanning-tree portfast
 spanning-tree bpduguard enable
interface FastEthernet0/3
 switchport mode access
 spanning-tree portfast
 spanning-tree bpduguard enable
interface FastEthernet0/4
 switchport mode access
 spanning-tree portfast
 spanning-tree bpduguard enable
"""
