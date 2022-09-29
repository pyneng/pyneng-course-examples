from pprint import pprint

devices = ["london_sw1", "london_sw2", "liverpool_sw1", "birmingham_sw1"]

vlans = {}
for key in devices:
    vlans[key] = []

vlans["london_sw1"].append(10)
pprint(vlans)

vlans = dict.fromkeys(devices, [])
vlans["london_sw1"].append(10)
pprint(vlans)

vlans = {key: [] for key in devices}
vlans["london_sw1"].append(10)
pprint(vlans)
