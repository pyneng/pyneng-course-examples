import re
from pprint import pprint

{
    "R1": {"ios": "12.4(24)T1", "ip": "10.1.1.1", "platform": "Cisco 3825"},
    "R2": {"ios": "15.2(2)T1", "ip": "10.2.2.2", "platform": "Cisco 2911"},
    "SW2": {"ios": "12.2(55)SE9", "ip": "10.1.1.2", "platform": "cisco WS-C2960-8TC-L"},
}

regex = (
    r"Device ID: (?P<device>\S+)"
    r"| +IP address: (?P<ip>\S+)"
    r"|Platform: (?P<platform>.+?),"
    r"|Version (?P<ios>\S+),"
    r"|Native VLAN: (?P<vlan>\d+)"
)
neighbors_dict = {}

file = "show_output/sh_cdp_neighbors_sw1.txt"
with open(file) as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            group = match.lastgroup
            if group == "device":
                device = match.group(group)
                neighbors_dict[device] = {}
            else:
                neighbors_dict[device][group] = match.group(group)

pprint(neighbors_dict, width=120)
