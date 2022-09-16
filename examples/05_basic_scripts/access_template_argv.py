import sys

print(sys.argv)
intf = sys.argv[1]
vlan = sys.argv[2]

access_str = """switchport mode access
switchport access vlan {}
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
"""

print(f"interface {intf}")
# print("interface {}".format(intf))
print(access_str.format(vlan))
