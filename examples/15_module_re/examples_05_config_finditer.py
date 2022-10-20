import re
from pprint import pprint


# regex = r"interface (\S+)[^!]+? ip address (\S+)"
regex = (
    r"interface (?P<intf>\S+)\n"
    r"(?: .+\n)*"
    r" ip address (?P<ip>\S+)"
)


intf_ip_dict = {}
cfg = "configs/config_r1.txt"
with open(cfg) as f:
    output = f.read()

match_all = re.finditer(regex, output)
for m in match_all:
    intf_ip_dict[m.group("intf")] = m.group("ip")

pprint(intf_ip_dict)
