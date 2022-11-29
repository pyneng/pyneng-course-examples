from pprint import pprint


class IPAddress:
    def __init__(self, ip, mask):
        print("__init__", ip, mask)
        self.ip = ip
        self.mask = mask

    def __str__(self):
        return f"{self.ip}/{self.mask}"

    def __repr__(self):
        return f"IPAddress('{self.ip}', {self.mask})"

    def __lt__(self, second_ip):
        print("__lt__", self, second_ip)
        return self.ip < second_ip.ip


ip1 = IPAddress("10.1.1.1", 25)
ip2 = IPAddress("10.2.2.2", 25)
ip3 = IPAddress("10.1.1.1", 25)
