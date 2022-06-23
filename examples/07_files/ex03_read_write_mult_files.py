from pprint import pprint

files = [
    "configs/config_r1.txt",
    "configs/config_sw1.txt",
    "configs/config_sw2.txt",
    "configs/config_r2.txt",
]

for filename in files:
    intf_ip_dict = {}
    with open(filename) as f:
        for line in f:
            if line.startswith("hostname"):
                hostname = line.split()[-1]
            elif line.startswith("interface"):
                intf = line.split()[-1]
                # print(f"{intf=}")
                # print(f"{hostname=} {intf=}")
            elif line.startswith(" ip address"):
                ip = line.split()[-2]
                print(f"{hostname=} {intf=} {ip=}")

