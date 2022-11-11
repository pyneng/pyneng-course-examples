from pprint import pprint
import os
from netmiko import Netmiko, NetmikoBaseException
from paramiko.ssh_exception import SSHException
import yaml


def get_show_output(device_params, show):
    try:
        with Netmiko(**device_params) as ssh:
            ssh.enable()
            out = ssh.send_command(show)
            return out
    except (NetmikoBaseException, SSHException) as error:
        print(error)


if __name__ == "__main__":
    with open("devices.yaml") as f:
        device_list = yaml.safe_load(f)

    passwd = os.environ.get("SSH_PASSWORD")
    enable = os.environ.get("SSH_ENABLE_PASSWORD")
    for device in device_list:
        device = {**device, "password": passwd, "secret": enable}
        result = get_show_output(device, "sh ip int br | i up.*up")
        pprint(result, width=120)
