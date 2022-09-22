commands = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

for cmd in commands:
    if "vlan" in cmd:
        print("Нашлась команда с vlan", cmd)
        break
else:
    print("В списке commands нет команды с vlan")
