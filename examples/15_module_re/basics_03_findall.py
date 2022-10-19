import re
from pprint import pprint

with open("sh_ip_int_br.txt") as f:
    output = f.read()

result = re.findall(r"(\S+) +([\d.]+)", output)
pprint(result)
