import re
from pprint import pprint

result = []
with open("sh_ip_int_br.txt") as f:
    for line in f:
        match = re.search(r"^(\S+) +([\d.]+)", line)
        if match:
            print(f"{match.group()=}")
            print(f"{match.groups()=}")
            result.append(match.groups())
pprint(result)
