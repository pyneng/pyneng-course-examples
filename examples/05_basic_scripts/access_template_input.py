from pprint import pprint
access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]
default_intf = "Gi0/0"
intf = input(f"Введите номер интерфейса [{default_intf}]: ")
vlan = input("Введите номер vlan: ")

print(f"interface {intf}")
access_str = "\n".join(access_template)
print(access_str.format(vlan))

input("Нажмите Enter для продложения")
