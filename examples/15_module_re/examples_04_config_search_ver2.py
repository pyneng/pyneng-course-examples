import re
from pprint import pprint


regex = (
    r"^interface (?P<intf>\S+)" # interface
    r"|^ ip address (?P<ip>\S+)" # ip address
)
intf_ip_dict = {}

cfg = "configs/config_r1.txt"
with open(cfg) as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            if match.lastgroup == "intf":
                intf = match.group("intf")
                intf_ip_dict[intf] = None
            elif match.lastgroup == "ip":
                ip = match.group("ip")
                intf_ip_dict[intf] = ip


pprint(intf_ip_dict)
