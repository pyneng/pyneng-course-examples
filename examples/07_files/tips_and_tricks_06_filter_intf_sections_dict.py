from pprint import pprint

{
    "Ethernet0/0": [
        "description To PE_r3 Ethernet0/0",
        "bandwidth 100000",
        "ip address 10.0.13.1 255.255.255.0",
        "mpls traffic-eng tunnels",
        "ip rsvp bandwidth 100000 10000",
    ],
    "Ethernet0/1": ["no ip address"],
    "Ethernet0/2": [
        "description To P_r9 Ethernet0/2",
        "ip address 10.0.19.1 255.255.255.0",
        "mpls traffic-eng tunnels",
        "ip rsvp bandwidth",
    ],
}

result = {}

src_file = "configs/config_r1.txt"
with open(src_file) as f:
    intf_section = False
    for line in f:
        if line.startswith("interface"):
            intf = line.split()[-1]
            intf_section = True
            result[intf] = []
        elif line.startswith(" "):
            if intf_section:
                result[intf].append(line.strip())
        else:
            intf_section = False

pprint(result)
