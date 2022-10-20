import re
from pprint import pprint


with open("sh_ip_int_br.txt") as f:
    output = f.read()

regex = r"Protocol\n(.+?)Loopback"

match = re.search(regex, output, re.DOTALL | re.DEBUG)
pprint(match)
if match:
    pprint(match.group(1))
