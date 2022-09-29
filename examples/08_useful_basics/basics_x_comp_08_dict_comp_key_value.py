from pprint import pprint

keys = ["hostname", "ip", "ios", "vendor"]
values = ["sw1", "10.1.1.1", "15.4", "Cisco"]

{'hostname': 'sw1', 'ios': '15.4', 'ip': '10.1.1.1', 'vendor': 'Cisco'}

device = dict(zip(keys, values))


# index
device = {}
for index in range(len(keys)):
    key = keys[index]
    value = values[index]
    device[key] = value
pprint(device)


device = {keys[index]: values[index] for index in range(len(keys))}
pprint(device)

# zip
device = {}
for key, value in zip(keys, values):
    device[key] = value
pprint(device)

device = {key: value for key, value in zip(keys, values)}
pprint(device)
