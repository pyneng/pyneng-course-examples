from pprint import pprint

keys = ["hostname", "ip", "ios", "vendor"]
values = ["sw1", "10.1.1.1", "15.4", "Cisco"]

device = {}
for key, value in zip(keys, values):
    device[key] = value
pprint(device)

device = dict(zip(keys, values))
pprint(device)

device = {key: value for key, value in zip(keys, values)}
pprint(device)
