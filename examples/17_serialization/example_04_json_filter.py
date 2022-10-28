from pprint import pprint
import json


with open("json_files/cfg.json") as f:
    data = json.load(f)

for value in data['configuration']['interfaces']['interface']:
    print(value["unit"])
    for item in value["unit"]:
        print(item["family"])

for n_ospf in data['ospf-neighbor-information']:
    for key, value in n_ospf.items():
        print(f"{key=} {value=}")
