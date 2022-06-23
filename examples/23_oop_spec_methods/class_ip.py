import ipaddress


class IPAddress:
    def __init__(self, ip):
        self.ip = ip

    def __repr__(self):
        return f"IPAddress('{self.ip}')"

    def __add__(self, number):
        if type(number) != int:
            raise TypeError(
                f"can only concatenate int (not {type(number).__name__})"
            )
        ip_as_int = int(self)
        result_int = ip_as_int + number
        result_ip = str(ipaddress.ip_address(result_int)) # "10.1.1.1"
        return IPAddress(result_ip)

    def __lt__(self, other):
        if type(other) != IPAddress:
            raise TypeError(
                f"can only compare int (not {type(number).__name__})"
            )
        return int(self) < int(other)

    def __le__(self, other):
        if type(other) != IPAddress:
            raise TypeError(
                f"can only compare int (not {type(number).__name__})"
            )
        return int(self) <= int(other)

    def __eq__(self, other):
        if type(other) != IPAddress:
            raise TypeError(
                f"can only compare int (not {type(number).__name__})"
            )
        return self.ip == other.ip

    def __int__(self):
        ip_as_int = int(ipaddress.ip_address(self.ip))
        return ip_as_int



if __name__ == "__main__":
    ip1 = IPAddress("10.1.1.1")
    ip2 = IPAddress("10.1.1.11")
    ip3 = IPAddress("10.1.1.10")
    ip4 = IPAddress("10.1.1.2")
    ip5 = IPAddress("10.1.1.1")
    ip1 + 5
    print(ip1 == ip5)
    print(int(ip1))
    ip_list = [ip1, ip2, ip3, ip4]
    print(ip_list)
    print(sorted(ip_list))
