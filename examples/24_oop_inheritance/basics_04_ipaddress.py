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
        return f"IPAddress('{self.ip}', {self.mask})"

    def __int__(self):
        print("__int__")
        int_ip = int(ipaddress.IPv4Address(self.ip))
        return int_ip

    def __lt__(self, second_ip):
        print(f"__lt__ {self=} {second_ip=}")
        if type(second_ip) != IPAddress:
            raise TypeError(
                f"'<' not supported between instances of 'IPAddress'"
                f" and '{type(second_ip).__name__}'"
            )
        return int(self) < int(second_ip)

    def __le__(self, second_ip):
        print(f"__le__ {self=} {second_ip=}")
        if type(second_ip) != IPAddress:
            raise TypeError(
                f"'<=' not supported between instances of 'IPAddress'"
                f" and '{type(second_ip).__name__}'"
            )
        return int(self) <= int(second_ip)

    def __eq__(self, second_ip):
        print(f"__eq__ {self=} {second_ip=}")
        if type(second_ip) != IPAddress:
            raise TypeError(
                f"'==' not supported between instances of 'IPAddress'"
                f" and '{type(second_ip).__name__}'"
            )
        return int(self) == int(second_ip)


ip1 = IPAddress("10.1.1.1", 25)
ip2 = IPAddress("10.2.2.2", 25)
ip3 = IPAddress("10.1.1.1", 25)
ip4 = IPAddress("10.10.1.1", 25)
ip5 = IPAddress("10.1.1.1", 29)
