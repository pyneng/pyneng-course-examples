import re
from pprint import pprint

regex = re.compile(r"^(\S+) +([\d.]+)")

result = []
with open("sh_ip_int_br.txt") as f:
    for line in f:
        match = regex.search(line)
        if match:
            result.append(match.groups())

pprint(result)
