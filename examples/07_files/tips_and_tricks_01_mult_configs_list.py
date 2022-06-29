from pprint import pprint

[
    ["PE_r1", "Loopback0", "10.1.1.1"],
    ["PE_r1", "Ethernet0/0", "10.0.13.1"],
    ["PE_r1", "Ethernet0/2", "10.0.19.1"],
    ["sw1", "Vlan100", "10.0.100.1"],
    ["sw2", "Vlan100", "10.0.100.2"],
    ["PE_r2", "Loopback0", "10.2.2.2"],
    ["PE_r2", "Ethernet0/0", "10.0.23.2"],
    ["PE_r2", "Ethernet0/1", "10.255.2.2"],
    ["PE_r2", "Ethernet0/2", "10.0.29.2"],
]


files = [
    "configs/config_r1.txt",
    "configs/config_sw1.txt",
    "configs/config_sw2.txt",
    "configs/config_r2.txt",
]

result = []

for filename in files:
    with open(filename) as f:
        for line in f:
            if line.startswith("hostname"):
                host = line.split()[-1]
            elif line.startswith("interface"):
                intf = line.split()[-1]
            elif line.startswith(" ip address"):
                ip = line.split()[2]
                # print(f"{host:15}{intf:20}{ip}")
                result.append([host, intf, ip])

pprint(result)
