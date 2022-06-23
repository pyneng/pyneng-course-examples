from pprint import pprint

result = {}

with open("configs/cfg.txt") as f:
    for line in f:
        if line.startswith("interface"):
            intf = line.split()[-1]
            # print(f"{intf=}")
        elif line.startswith(" ip address"):
            ip = line.split()[-2]
            print(f"{intf=} {ip=}")

# pprint(result)
