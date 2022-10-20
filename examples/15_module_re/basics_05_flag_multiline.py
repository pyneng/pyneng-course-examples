import re
from pprint import pprint

regex = r"^(\S+) +([\d.]+)"

result = []
with open("sh_ip_int_br.txt") as f:
    output = f.read()

m_all = re.finditer(regex, output, re.MULTILINE)
for m in m_all:
    print(m.groups())

pprint(result)

# compile
regex = re.compile(r"^(\S+) +([\d.]+)", re.MULTILINE)

result = []
with open("sh_ip_int_br.txt") as f:
    output = f.read()

m_all = regex.finditer(output)
for m in m_all:
    print(m.groups())

pprint(result)
