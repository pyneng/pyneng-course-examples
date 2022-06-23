from sys import argv
# import sys
print(argv)
intf = argv[1]
vlan = argv[2]

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

print(f"interface {intf}")
access_str = "\n".join(access_template)
print(access_str.format(vlan))
