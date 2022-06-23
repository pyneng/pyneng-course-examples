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

    def __len__(self):
        return len(self.hosts)

    def __getitem__(self, index):
        print("__getitem__", index)
        return self.hosts[index]

    #def __iter__(self):
    #    print("__iter__")
    #    return iter(self.hosts) # iterator

if __name__ == "__main__":
    net1 = Network("10.1.1.0", 29)
    print(net1)
    print(net1.hosts)
