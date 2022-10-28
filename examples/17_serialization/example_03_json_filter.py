from pprint import pprint
import json


with open("json_files/cfg.json") as f:
    data = json.load(f)

for value in data["configuration"]["interfaces"]["interface"]:
    pprint(value)

for ospf in data["ospf-neighbor-information"]:
    pprint(ospf)
