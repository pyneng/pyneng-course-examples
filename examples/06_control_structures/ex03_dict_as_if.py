from pprint import pprint

cfg = input("Введите что надо настроить: ")

if cfg == "access":
    print("access_cfg")
elif cfg == "trunk":
    print("trunk_cfg")
elif cfg == "vpn":
    print("vpn_cfg")
else:
    print("такой конфигурации нет")


choices = {
    "access": "access_cfg",
    "trunk": "trunk_cfg",
    "vpn": "vpn_cfg",
}
value = choices.get(cfg)
pprint(value)
print(f"{value=}")
if value:
    print(value)
else:
    print("такой конфигурации нет")
