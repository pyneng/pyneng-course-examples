from pprint import pprint

devices = ["london_sw1", "london_sw2", "liverpool_sw1", "birmingham_sw1"]

{'birmingham_sw1': None,
 'liverpool_sw1': None,
 'london_sw1': None,
 'london_sw2': None}

dev_dict = {}
for key in devices:
    dev_dict[key] = None

pprint(dev_dict)

dev_dict = dict.fromkeys(devices)
pprint(dev_dict)

dev_dict = {key: None for key in devices}
pprint(dev_dict)
