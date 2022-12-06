from pprint import pprint
import subprocess
from concurrent.futures import ThreadPoolExecutor
from netmiko import ConnectHandler
import paramiko
import yaml



class ScanDevices:
    def __init__(self, device_list):
        self.device_list = device_list

    def _scan_device(self, ip):
        print("scanning...")
        result = subprocess.run(
            ["ping", "-c", "3", "-n", ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
        )
        if result.returncode == 0:
            return True
        else:
            return False

    def scan(self, max_threads=5):
        scan_ok = []
        scan_not_ok = []
        with ThreadPoolExecutor(max_workers=max_threads) as ex:
            result_all = ex.map(self._scan_device, self.device_list)
            for dev, status in zip(self.device_list, result_all):
                if status:
                    scan_ok.append(dev)
                else:
                    scan_not_ok.append(dev)
        return scan_ok, scan_not_ok

if __name__ == "__main__":
    # Ping scan
    s = ScanDevices(["8.8.8.8", "8.8.4.4", "10.1.1.1"])
    pprint(s.scan(), width=120)
