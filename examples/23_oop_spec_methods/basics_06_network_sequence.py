import ipaddress


class Network:
    def __init__(self, network, mask):
        self.network = network
        self.mask = mask

    def __str__(self):
        return f"{self.network}/{self.mask}"

    def __repr__(self):
        return f"Network('{self.network}', {self.mask})"


if __name__ == "__main__":
    net1 = Network("10.1.1.0", 29)
    print(net1)
    print(net1.hosts)
