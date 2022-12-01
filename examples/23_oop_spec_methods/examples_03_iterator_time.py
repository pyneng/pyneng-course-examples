from datetime import datetime
from netmiko import Netmiko, NetmikoBaseException
import yaml


def get_show_output(device_params, show):
    with Netmiko(**device_params) as ssh:
        ssh.enable()
        out = ssh.send_command(show)
        return out


class CurrentTime:
    def __next__(self):
        print("__next__")
        now = datetime.now()
        return str(now)

    def __iter__(self):
        print("__iter__")
        return self


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    ct = CurrentTime()

    print(f"{next(ct)} START")
    for device, ctime in zip(devices, ct):
        out = get_show_output(device, "sh run | i hostname")
        print(ctime)
        print(out)
