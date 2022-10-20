import re
from pprint import pprint


regex = (
    r"^(interface \S+.+?)!"
)


cfg = "configs/config_r1.txt"
with open(cfg) as f:
    output = f.read()

match_all = re.finditer(regex, output, re.MULTILINE | re.DOTALL)
for m in match_all:
    print(m.group(1))
    print("=" * 40)

