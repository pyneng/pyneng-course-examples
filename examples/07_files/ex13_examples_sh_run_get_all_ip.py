from pprint import pprint

ip_list = []

file = "configs/cfg.txt"
with open(file) as f:
    for line in f:
        if line.startswith(" ip address"):
            words = line.split()
            ip = words[2]
            # ip = line.split()[2]
            ip_list.append(ip)
print(ip_list)
