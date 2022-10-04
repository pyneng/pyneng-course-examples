"""
[['FastEthernet0/0', '15.0.15.1', 'up'],
 ['FastEthernet0/1', '10.0.12.1', 'up'],
 ['FastEthernet0/2', '10.0.13.1', 'down'],
 ['FastEthernet0/3', 'unassigned', 'down'],
 ['Loopback0', '10.1.1.1', 'up'],
 ['Loopback100', '100.0.0.1', 'up']]
"""
from pprint import pprint


def parse_sh_ip_int_br(output):
    result_list = []
    for line in output.split("\n"):
        if "up" in line or "down" in line:
            intf, ip, *_, status = line.split()
            result_list.append([intf, ip, status])
    return result_list


def count_ports(sh_ip_int_br_list):
    up = 0
    down = 0
    for intf, ip, status in sh_ip_int_br_list:
        if status == "up":
            up += 1
        elif status == "down":
            down += 1
    return up, down



def count_ports_2(sh_ip_int_br_list):
    result_dict = {
        "up": 0,
		"down": 0,
    }
    for intf, ip, status in sh_ip_int_br_list:
        if status == "up":
            result_dict["up"] += 1
        elif status == "down":
            result_dict["down"] += 1
    return result_dict



file = "show_output/sh_ip_int_br.txt"
with open(file) as f:
    content = f.read()

result = parse_sh_ip_int_br(content)
pprint(result)
pprint(count_ports_2(result), sort_dicts=False)
