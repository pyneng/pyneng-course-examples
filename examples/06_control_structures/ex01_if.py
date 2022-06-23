from pprint import pprint
access_template = (
    "switchport mode access\n"
    "switchport access vlan {}\n"
    "switchport nonegotiate\n"
    "spanning-tree portfast\n"
    "spanning-tree bpduguard enable\n"
)

trunk_template = (
    "switchport trunk encapsulation dot1q\n"
    "switchport mode trunk\n"
    "switchport trunk allowed vlan {}\n"
)

mode = input("Введите режим: ")
vlan = input("Введите влан: ")
mode = mode.lower().strip()

print(f"{mode=}") # Python version >= 3.8
# pprint(mode) # Python version < 3.8
if mode == "access":
    print(access_template.format(vlan))
elif mode == "trunk":
    print(trunk_template.format(vlan))
else:
    print("Такого режима нет")
