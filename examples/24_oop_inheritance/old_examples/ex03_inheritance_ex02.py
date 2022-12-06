from ex02_scan_devices import ScanDevices
from netmiko import Netmiko
from netmiko.exceptions import NetmikoBaseException
from paramiko.ssh_exception import SSHException
import yaml
from pprint import pprint


class ScanNetmikoSSH(ScanDevices):
    def _scan_device(self, device_params):
        try:
            with Netmiko(**device_params) as ssh:
                ssh.enable()
            return True
        except (NetmikoBaseException, SSHException):
            return False


if __name__ == "__main__":
    with open("devices.yaml") as f:
        ssh_devices = yaml.safe_load(f)
    sc = ScanNetmikoSSH(ssh_devices)
    pprint(sc.scan())
