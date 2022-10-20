import re
from pprint import pprint


regex_intf = r"^interface (\S+)"
regex_ip = r"^ ip address (\S+)"
intf_ip_dict = {}

cfg = "configs/config_r1.txt"
with open(cfg) as f:
    for line in f:
        match_intf = re.search(regex_intf, line)
        match_ip = re.search(regex_ip, line)
        if match_intf:
            intf = match_intf.group(1)
            # intf_ip_dict[intf] = None
        elif match_ip:
            ip = match_ip.group(1)
            intf_ip_dict[intf] = ip

pprint(intf_ip_dict)
