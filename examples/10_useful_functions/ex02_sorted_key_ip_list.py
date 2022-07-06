from pprint import pprint

ip_list = ["10.1.1.1", "10.2.2.2", "10.100.1.1", "1.100.100.1"]
print(sorted(ip_list))

# def delete_dot(ip):
#     return int(ip.replace(".", ""))
#
# print(sorted(ip_list, key=delete_dot))


def ip_to_bin(ip):
    octets = []
    for o in ip.split("."):
        octet = f"{int(o):08b}"
        octets.append(octet)
    return "".join(octets)


print(sorted(ip_list, key=ip_to_bin))

