import re
from pprint import pprint


regex = (
    r"^interface \S+\n"
    r"(?: .+\n)+"
)


cfg = "configs/config_r1.txt"
with open(cfg) as f:
    output = f.read()

match_all = re.finditer(regex, output, re.MULTILINE)
for m in match_all:
    print(m.group())
    print("=" * 40)

