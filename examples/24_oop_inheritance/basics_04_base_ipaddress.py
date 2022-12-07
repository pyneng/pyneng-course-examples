import ipaddress
from pprint import pprint


class IPAddress:
    def __init__(self, ip, mask):
        print(f"__init__ {ip=} {mask=}")
        self.ip = ip
        self.mask = mask

    def __str__(self):
        return f"{self.ip}/{self.mask}"

    def __repr__(self):
        return f"{type(self).__name__}('{self.ip}', {self.mask})"

    def __lt__(self, second_ip):
        print(f"__lt__ {self=} {second_ip=}")
        if type(second_ip) != IPAddress:
            raise TypeError(f"'<' not supported between instances of 'IPAddress'"
                            f" and '{type(second_ip).__name__}'")
        return (int(self), self.mask) < (int(second_ip), second_ip.mask)

    def __le__(self, second_ip):
        print(f"__le__ {self=} {second_ip=}")
        if type(second_ip) != IPAddress:
            raise TypeError(f"'<=' not supported between instances of 'IPAddress'"
                            f" and '{type(second_ip).__name__}'")
        return (int(self), self.mask) <= (int(second_ip), second_ip.mask)

    def __eq__(self, second_ip):
        print(f"__eq__ {self=} {second_ip=}")
        if type(second_ip) != IPAddress:
            raise TypeError(f"'==' not supported between instances of 'IPAddress'"
                            f" and '{type(second_ip).__name__}'")
        return (int(self), self.mask) == (int(second_ip), second_ip.mask)



class IPv4Address(IPAddress):
    def __int__(self):
        int_ip = int(ipaddress.IPv4Address(self.ip))
        return int_ip


class IPv6Address(IPAddress):
    def __int__(self):
        print(f"__int__ {self=}")
        int_ip = int(ipaddress.IPv6Address(self.ip))
        return int_ip

ip1 = IPv4Address("10.1.1.1", 25)
ip2 = IPv4Address("10.2.2.2", 25)
ip3 = IPv4Address("10.1.1.1", 25)
ip4 = IPv4Address("10.10.1.1", 25)

