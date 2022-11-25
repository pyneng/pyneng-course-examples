import sys
from pprint import pprint
import textfsm
from tabulate import tabulate

template = sys.argv[1]
output_file = sys.argv[2]

with open(output_file) as output:
    cmd_output = output.read()

with open(template) as t:
    fsm = textfsm.TextFSM(t)
    header = fsm.header
    result = fsm.ParseText(cmd_output)
    pprint(result, width=120)
    print()
    print(tabulate(result, headers=header))
