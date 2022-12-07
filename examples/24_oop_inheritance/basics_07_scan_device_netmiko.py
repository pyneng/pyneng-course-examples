from pprint import pprint
from netmiko import Netmiko
from netmiko.exceptions import NetmikoBaseException
from paramiko.ssh_exception import SSHException
import yaml

from basics_06_scan_device_base import ScanDevices


class ScanNetmikoSSH(ScanDevices):
    def _scan_device(self, device_params):
        try:
            with Netmiko(**device_params) as ssh:
                ssh.enable()
            return True
        except (NetmikoBaseException, SSHException):
            return False



if __name__ == "__main__":
    with open("devices_netmiko.yaml") as f:
        devices = yaml.safe_load(f)
    sd = ScanNetmikoSSH(devices)
    pprint(sd.scan())
