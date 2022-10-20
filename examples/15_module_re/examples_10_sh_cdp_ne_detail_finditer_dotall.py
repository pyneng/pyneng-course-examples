import re
from pprint import pprint

{
    "R1": {"ios": "12.4(24)T1", "ip": "10.1.1.1", "platform": "Cisco 3825"},
    "R2": {"ios": "15.2(2)T1", "ip": "10.2.2.2", "platform": "Cisco 2911"},
    "SW2": {"ios": "12.2(55)SE9", "ip": "10.1.1.2", "platform": "cisco WS-C2960-8TC-L"},
}

regex = (
    r"Device ID: (?P<device>\S+)"
    r".+?"
    r" +IP address: (?P<ip>\S+)\n"
    r"Platform: (?P<platform>.+?),"
    r".+?"
    r"Cisco IOS .+? Version (?P<ios>\S+),"
)

file = "show_output/sh_cdp_neighbors_sw1.txt"
with open(file) as f:
    output = f.read()

neighbors_dict = {}
match_all = re.finditer(regex, output, re.DOTALL)
for m in match_all:
    gdict = m.groupdict()
    device = gdict.pop("device")
    neighbors_dict[device] = gdict

pprint(neighbors_dict, width=120)
