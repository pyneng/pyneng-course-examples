from pprint import pprint


result = []

file = "show_output/sh_ip_int_br.txt"
with open(file) as f:
    for line in f:
        if "up" in line or "down" in line:
            intf, ip, ok, method, status, protocol = line.split()
            new_list = [protocol, intf, ip]
            result.append(new_list)

pprint(result)
sorted_data = sorted(result)
pprint(sorted_data)

for status, intf, ip in sorted_data:
    print(f"{intf:20}{ip:15}{status}")
