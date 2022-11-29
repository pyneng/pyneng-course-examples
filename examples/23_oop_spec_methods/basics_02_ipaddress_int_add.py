import ipaddress
from pprint import pprint


class IPAddress:
    def __init__(self, ip, mask):
        print(f"__init__ {ip=} {mask=}")
        self.ip = ip
        self.mask = mask

    def __str__(self):
        print("__str__")
        return f"{self.ip}/{self.mask}"

    def __repr__(self):
        # print("__repr__")
        return f"IPAddress('{self.ip}', {self.mask})"

    def __int__(self):
        print(f"__int__ {self=}")
        octets = [f"{int(octet):08b}" for octet in self.ip.split(".")]
        bin_ip = "".join(octets)
        return int(bin_ip, 2)

    def __add__(self, integer):
        print(f"__add__ {self=} {integer=}")
        if not isinstance(integer, int):
            raise TypeError(
                f"unsupported operand type(s) for +: 'IPAddress' and "
                f"'{type(integer).__name__}'"
            )
        new_ip_int = int(self) + integer
        new_ip = str(ipaddress.ip_address(new_ip_int))
        return IPAddress(new_ip, self.mask)



ip1 = IPAddress("10.1.1.1", 25)
ip2 = IPAddress("10.2.2.2", 25)
ip3 = IPAddress("10.1.1.1", 25)
ip4 = IPAddress("10.10.1.1", 25)
