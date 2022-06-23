import sys
from pprint import pprint
import textfsm
from tabulate import tabulate

template = sys.argv[1]
output_file = sys.argv[2]

with open(template) as f, open(output_file) as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    # result = re_table.ParseTextToDicts(output.read())
    pprint([dict(zip(header, item)) for item in result], sort_dicts=False)
