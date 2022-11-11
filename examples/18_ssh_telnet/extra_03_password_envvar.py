from pprint import pprint
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
    for device in device_list:
        result = get_show_output(device, "sh ip int br | i up.*up")
        pprint(result, width=120)
