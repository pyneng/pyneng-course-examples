from pprint import pprint
access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

access_str = "\n".join(access_template)
print(access_str.format(100))
