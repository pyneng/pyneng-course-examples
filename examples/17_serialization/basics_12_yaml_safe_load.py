from pprint import pprint
import yaml


file = "yaml_files/info.yaml"
with open(file) as f:
    data = yaml.safe_load(f)

pprint(data)
