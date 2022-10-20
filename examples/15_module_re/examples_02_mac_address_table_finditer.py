from pprint import pprint
import re

regex = r"(\d+) +(\S+) +\w+ +(\S+)"

filename = "show_output/sh_mac_address.txt"
with open(filename) as f:
    output = f.read()

result = []
match_all = re.finditer(regex, output)
for m in match_all:
    result.append(m.groups())

pprint(result)
