commands = [
    "switchport mode access",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

for cmd in commands:
    if "vlan" in cmd:
        print("Нашли команду с vlan")
        break
else: # no break
    print("В списке commands нет команды с vlan")
