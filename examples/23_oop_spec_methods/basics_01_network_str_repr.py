from pprint import pprint
import ipaddress


class Network:
    def __init__(self, network, mask):
        self.network = network
        self.mask = mask
        ipv4net = ipaddress.ip_network(f"{self.network}/{self.mask}")
        self.hosts = [str(ip) for ip in ipv4net.hosts()]

    def __str__(self):
        return f"{self.network}/{self.mask}"

    def __repr__(self):
        return f"Network('{self.network}', {self.mask})"


net1 = Network("10.1.1.0", 28)
net2 = Network("10.2.2.0", 28)

print(net1)
pprint(net1)
print(f"Example {repr(net1)}")
