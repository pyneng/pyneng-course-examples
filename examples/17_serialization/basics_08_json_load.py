import json
from pprint import pprint

file = "json_files/sw_templates.json"

with open(file) as f:
    data = json.load(f)

pprint(data)
