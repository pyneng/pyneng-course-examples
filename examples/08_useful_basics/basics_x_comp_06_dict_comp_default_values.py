from pprint import pprint

devices = ["london_sw1", "london_sw2", "liverpool_sw1", "birmingham_sw1"]

vlans = {}
for key in devices:
    vlans[key] = None

pprint(vlans)

vlans = dict.fromkeys(devices)
pprint(vlans)

vlans = {key: None for key in devices}
pprint(vlans)
