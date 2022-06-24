"""
{'FastEthernet0/0': '15.0.15.1',
 'FastEthernet0/1': '10.0.12.1',
 'FastEthernet0/2': '10.0.13.1',
 'FastEthernet0/3': None,
 'Loopback0': '10.1.1.1',
 'Loopback100': '100.0.0.1'}
"""
from pprint import pprint

intf_ip_dict = {}

file = "show_output/sh_ip_int_br.txt"
with open(file) as f:
    for line in f:
        if "up" in line or "down" in line:
            words = line.split()
            intf = words[0]
            ip = words[1]
            if ip == "unassigned":
                intf_ip_dict[intf] = None
            else:
                intf_ip_dict[intf] = ip

pprint(intf_ip_dict)

for intf, ip in intf_ip_dict.items():
    if ip:
        print(ip)
