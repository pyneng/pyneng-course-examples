line = "Ethernet0/0                192.168.100.1   YES NVRAM  up                    up"

line.split()
['Ethernet0/0', '192.168.100.1', 'YES', 'NVRAM', 'up', 'up']

words = line.split()
intf = words[0]
ip = words[1]
status = words[-1]

intf, ip, *_, status = words
print(intf, ip, status)


for _ in range(5):
    print("-" * 40)

