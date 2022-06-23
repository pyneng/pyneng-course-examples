from pprint import pprint


result = {}

with open("show_output/sh_ip_int_br.txt") as f:
    for line in f:
        words = line.split()
        # if words != []:
        # if words:
        # только с IP
        # if len(words) >= 6 and words[1][0].isdigit():
        # полезные данные
        if len(words) >= 6 and words[0][-1].isdigit():
            # pprint(words)
            intf = words[0]
            ip = words[1]
            # intf, ip = words[:2]
            print(intf, ip)
            if ip == "unassigned":
                result[intf] = None
            else:
                result[intf] = ip

pprint(result)

for intf, ip in result.items():
    if ip:
        print(ip)
