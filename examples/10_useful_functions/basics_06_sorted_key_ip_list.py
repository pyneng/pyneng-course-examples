

ip_list = ["10.1.1.1", "10.2.2.2", "10.100.1.1", "1.100.100.1"]


def ip_to_bin(ip):
    octets = ip.split(".")
    bin_ip = ""
    for octet in octets:
        oct_bin = f"{int(octet):08b}"
        bin_ip += oct_bin
    return bin_ip


def ip_to_int(ip):
    bin_ip = ip_to_bin(ip)
    return int(bin_ip, 2)


print(sorted(ip_list))
print(sorted(ip_list, key=ip_to_bin))
print(sorted(ip_list, key=ip_to_int))
