from pprint import pprint


cfg = "configs/cfg.txt"

with open(cfg) as f:
    for line in f:
        if line.startswith("interface"):
            intf = line.split()[-1]
            # print(f"{intf=}") # Python >= 3.8
        elif line.startswith(" ip address"):
            ip = line.split()[2]
            print(f"{intf:20} {ip}")

