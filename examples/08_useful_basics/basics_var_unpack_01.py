line = "Ethernet0/0                192.168.100.1   YES NVRAM  up                    up"


columns = line.split()
# ['Ethernet0/0', '192.168.100.1', 'YES', 'NVRAM', 'up', 'up']

intf = columns[0]
ip = columns[1]
status = columns[-1]

