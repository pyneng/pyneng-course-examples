import subprocess
from concurrent.futures import ThreadPoolExecutor

from class_network import Network


class NetworkScanner:
    def __init__(self, network):
        self.network = network

    def _ping_ip(self, ip):
        result = subprocess.run(
            f"ping -c 3 {ip}".split(), stdout=subprocess.PIPE
        )
        if result.returncode == 0:
            return True
        else:
            return False

    def scan(self, max_workers=3):
        ok = []
        not_ok = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = executor.map(self._ping_ip, self.network)
            for ip, status in zip(self.network, results):
                if status:
                    ok.append(ip)
                else:
                    not_ok.append(ip)
        return ok, not_ok


if __name__ == "__main__":
    net1 = Network("192.168.100.0", 29)
    scanner = NetworkScanner(net1)
    ok, not_ok = scanner.scan()
    print(ok)
    print(not_ok)
