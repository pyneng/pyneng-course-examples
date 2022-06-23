from pprint import pprint

files = [
    "configs/config_r1.txt",
    "configs/config_sw1.txt",
    "configs/config_sw2.txt",
    "configs/config_r2.txt",
]

result = {}

for filename in files:
    with open(filename) as f:
        for line in f:
            if line.startswith("hostname"):
                hostname = line.split()[-1]
                result[hostname] = {}
            elif line.startswith("interface"):
                intf = line.split()[-1]
            elif line.startswith(" ip address"):
                ip = line.split()[-2]
                result[hostname][intf] = ip


pprint(result)
{
    "PE_r1": {
        "Loopback0": "10.1.1.1",
        "Ethernet0/0": "10.0.13.1",
        "Ethernet0/2": "10.0.19.1",
    },
    "sw1": {"Vlan100": "10.0.100.1"},
    "sw2": {"Vlan100": "10.0.100.2"},
}
