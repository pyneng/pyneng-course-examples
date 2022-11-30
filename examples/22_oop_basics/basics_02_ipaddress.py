class IPAddress:
    def __init__(self, ip, mask):
        self.address = ip
        self.mask = mask

    def info(self):
        print(f"IP address\nIP {self.address}")


ip1 = IPAddress("10.1.1.1", 24)
ip2 = IPAddress("10.2.2.2", 24)

print(f"{ip1.address=}")
print(f"{ip1.mask=}")
print(f"{ip2.address=}")
print(f"{ip2.mask=}")
ip1.info()
ip2.info()

