from pprint import pprint


def ip_to_bin(ip):
    octets = []
    for o in ip.split("."):
        octet = f"{int(o):08b}"
        octets.append(octet)
    return "".join(octets)


ip_list = ["10.1.1.1", "10.2.2.2", "10.100.1.1", "1.100.100.1"]

data_to_sort = []
for ip in ip_list:
    data_to_sort.append([ip_to_bin(ip), ip])

sorted_by_bin = sorted(data_to_sort)
pprint(sorted_by_bin)

sorted_ip = []
for bin_ip, ip in sorted_by_bin:
    sorted_ip.append(ip)

pprint(sorted_ip)
