from pprint import pprint

filename = "show_output/sh_ip_int_br.txt"
with open(filename) as f:
    for line in f:
        if "up" in line or "down" in line:
            words = line.split()
            intf = words[0]
            ip = words[1]
            # print("{:20}{}".format(intf, ip))
            print(f"{intf:20}{ip}")
