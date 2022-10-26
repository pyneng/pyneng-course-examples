from pprint import pprint
import yaml

file = "yaml_files/london_params.yaml"
with open(file) as f:
    data = yaml.safe_load(f)

    pprint(data, sort_dicts=False)
