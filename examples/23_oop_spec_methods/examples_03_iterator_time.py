from datetime import datetime
from netmiko import Netmiko, NetmikoBaseException
import yaml


class CurrentTime:
    def __next__(self):
        print("__next__")
        now = datetime.now()
        return str(now)

    def __iter__(self):
        return self


def get_show_output(device_params, show):
    with Netmiko(**device_params) as ssh:
        ssh.enable()
        out = ssh.send_command(show)
        return out


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    ct = CurrentTime()
    for device, ctime in zip(devices, ct):
        print(ctime)
        output = get_show_output(device, "sh run | i hostname")
        print(output)
        output = get_show_output(device, "sh run | i alias")
        print(output)
