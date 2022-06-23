from pprint import pprint


with open("show_output/sh_ip_int_br.txt") as f:
    for line in f:
        words = line.split()
        if len(words) >= 6 and words[0][-1].isdigit():
            intf = words[0]
            ip = words[1]
            print(f"{intf:20}{ip}")
