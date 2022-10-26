from pprint import pprint
import yaml

file = "yaml_files/mult_docs.yaml"
with open(file) as f:
    data = yaml.safe_load_all(f)

    pprint(list(data))
    # for item in data:
    #    pprint(item)
