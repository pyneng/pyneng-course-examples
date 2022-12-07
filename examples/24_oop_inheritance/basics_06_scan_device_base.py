from concurrent.futures import ThreadPoolExecutor
import subprocess
from pprint import pprint


class ScanDevices:
    def __init__(self, device_list):
        self.device_list = device_list

    def _scan_device(self, ip):
        print(f"ping {ip}")
        result = subprocess.run(
            ["ping", "-c", "3", "-n", ip],
            capture_output=True,
            encoding="utf-8",
        )
        if result.returncode == 0:
            return True
        else:
            return False

    def scan(self, limit=5):
        scan_success = []
        scan_fail = []
        with ThreadPoolExecutor(limit) as ex:
            result_all = ex.map(self._scan_device, self.device_list)
            for device, status in zip(self.device_list, result_all):
                if status:
                    scan_success.append(device)
                else:
                    scan_fail.append(device)
        return scan_success, scan_fail



if __name__ == "__main__":
    sd = ScanDevices(["8.8.8.8", "192.168.100.1", "10.1.1.1"])
    pprint(sd.scan())
