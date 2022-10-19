import re
from pprint import pprint

result = []
with open("sh_ip_int_br.txt") as f:
    output = f.read()

m_all = re.finditer(r"(\S+) +([\d.]+)", output)
for m in m_all:
    result.append(m.groups())

pprint(result)
