class IPAddress:
    def __init__(self, ip, mask):
        self.address = ip
        self.mask = mask
        self.bin_mask = self._mask_to_bin()
        self.dec_mask = self._mask_to_dec()

    def info(self):
        print(f"IP address\nIP {self.address}")

    def to_bin(self):
        octets = [f"{int(octet):08b}" for octet in self.address.split(".")]
        return "".join(octets)

    def _mask_to_bin(self):
        bin_mask = "1" * self.mask + "0" * (32 - self.mask)
        return bin_mask

    def _mask_to_dec(self):
        dec_mask = ".".join([
            str(int(self.bin_mask[index: index + 8], 2)) for index in range(0, 25, 8)
        ])
        return dec_mask


ip1 = IPAddress("10.1.1.1", 24)
ip2 = IPAddress("10.2.2.2", 24)


