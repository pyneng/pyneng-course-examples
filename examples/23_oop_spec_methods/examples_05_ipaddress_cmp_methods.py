import ipaddress
from pprint import pprint


class IPAddress:
    def __init__(self, ip, mask):
        print(f"__init__ {ip=} {mask=}")
        self.ip = ip
        self.mask = mask
        self._int_ip = int(ipaddress.ip_address(self.ip))

    def __str__(self):
        return f"{self.ip}/{self.mask}"

    def __repr__(self):
        return f"IPAddress('{self.ip}', {self.mask})"

    def __lt__(self, second_ip):
        print(f"__lt__ {self=} {second_ip=}")
        if type(second_ip) != IPAddress:
            raise TypeError(f"'<' not supported between instances of 'IPAddress'"
                            f" and '{type(second_ip).__name__}'")
        return (self._int_ip, self.mask) < (second_ip._int_ip, second_ip.mask)

    def __le__(self, second_ip):
        print(f"__le__ {self=} {second_ip=}")
        if type(second_ip) != IPAddress:
            raise TypeError(f"'<=' not supported between instances of 'IPAddress'"
                            f" and '{type(second_ip).__name__}'")
        return (self._int_ip, self.mask) <= (second_ip._int_ip, second_ip.mask)

    def __eq__(self, second_ip):
        print(f"__eq__ {self=} {second_ip=}")
        if type(second_ip) != IPAddress:
            raise TypeError(f"'==' not supported between instances of 'IPAddress'"
                            f" and '{type(second_ip).__name__}'")
        return (self._int_ip, self.mask) == (second_ip._int_ip, second_ip.mask)

ip1 = IPAddress("10.1.1.1", 25)
ip2 = IPAddress("10.2.2.2", 25)
ip3 = IPAddress("10.1.1.1", 25)
ip4 = IPAddress("10.10.1.1", 25)
ip5 = IPAddress("10.1.1.1", 29)


#    def __lt__(self, second_ip):
#        return self._int_ip < second_ip._int_ip
#        if self._int_ip < second_ip._int_ip:
#            return True
#        else:
#            return False
