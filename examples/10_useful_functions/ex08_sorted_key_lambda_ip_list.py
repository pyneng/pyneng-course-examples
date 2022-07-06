from pprint import pprint

ip_list = ["10.1.1.1", "10.2.2.2", "10.100.1.1", "1.100.100.1"]
print(sorted(ip_list))


def ip_to_bin(ip):
    """
    Преобразует IP в двоичный формат
    """
    octets = []
    for o in ip.split("."):
        octet = f"{int(o):08b}"
        octets.append(octet)
    # octets = [f"{intf(o):08b}" for o in ip.split(".")]
    return "".join(octets)


print(sorted(
    ip_list,
    key=lambda ip: "".join([f"{intf(o):08b}" for o in ip.split(".")])
))

