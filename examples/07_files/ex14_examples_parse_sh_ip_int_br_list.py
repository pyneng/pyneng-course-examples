"""
[['FastEthernet0/0', '15.0.15.1', 'up'],
 ['FastEthernet0/1', '10.0.12.1', 'up'],
 ['FastEthernet0/2', '10.0.13.1', 'down'],
 ['FastEthernet0/3', 'unassigned', 'down'],
 ['Loopback0', '10.1.1.1', 'up'],
 ['Loopback100', '100.0.0.1', 'up']]
"""
from pprint import pprint

result = []

file = "show_output/sh_ip_int_br.txt"
with open(file) as f:
    for line in f:
        if "up" in line or "down" in line:
            words = line.split()
            intf = words[0]
            ip = words[1]
            status = words[-1]
            data = [intf, ip, status]
            result.append(data)

pprint(result)
