from pprint import pprint

files = [
    "configs/config_r1.txt",
    "configs/config_sw1.txt",
    "configs/config_sw2.txt",
    "configs/config_r2.txt",
]

result = {}

for filename in files:
    intf_ip_dict = {}
    with open(filename) as f:
        for line in f:
            if line.startswith("hostname"):
                hostname = line.split()[-1]
            elif line.startswith("interface"):
                intf = line.split()[-1]
            elif line.startswith(" ip address"):
                ip = line.split()[-2]
                intf_ip_dict[intf] = ip
    result[hostname] = intf_ip_dict


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
