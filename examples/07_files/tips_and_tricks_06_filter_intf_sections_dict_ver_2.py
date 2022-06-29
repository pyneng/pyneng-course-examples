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

with open("configs/config_r1.txt") as src:
    for line in src:
        if not line.startswith(" "):
            section = line.strip()
        else:
            if section.startswith("interface"):
                if section not in result:
                    result[section] = []
                result[section].append(line.strip())

pprint(result)
