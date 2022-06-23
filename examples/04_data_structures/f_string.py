from pprint import pprint
template = "{:<20}{:<4}{:6}"
print(template.format("10.1.1.1", 24, "g0/0"))
print(template.format("192.168.1.1", 8, "g0/1"))
print(template.format("10.2.2.101", 24, "g0/2"))
# pprint(template.format("10.1.1.1", 24, "g0/0"))
# pprint(template.format("192.168.1.1", 8, "g0/1"))
# pprint(template.format("10.2.2.101", 24, "g0/2"))

ip = "10.1.1.1"
mask = 24
intf = "g0/0"
print(f"{ip:20}{mask}{intf}")
ip = "10.2.2.2"
mask = 24
intf = "g0/0"
print(f"{ip:20}{mask}{intf}")
