
from pprint import pprint

def grep_cfg(filename, pattern):
    lines = []
    with open(filename) as f:
        for line in f:
            if pattern in line:
                lines.append(line)
    return lines


result = grep_cfg("configs/config_r1.txt", "ip address")
pprint(result)
pprint(grep_cfg("configs/config_r1.txt", pattern="alias"))

