from pprint import pprint

devices = ["london_sw1", "london_sw2", "liverpool_sw1", "birmingham_sw1"]

{'birmingham_sw1': [],
 'liverpool_sw1': [],
 'london_sw1': [],
 'london_sw2': []}

# vlans = dict.fromkeys(devices, [])
# vlans["london_sw2"].append(100)
# pprint(vlans)

vlans = {}
for key in devices:
    vlans[key] = []

vlans["london_sw2"].append(100)
pprint(vlans)

vlans = {key: [] for key in devices}
vlans["london_sw2"].append(100)
pprint(vlans)
