from pprint import pprint
from netmiko import Netmiko, NetmikoBaseException
from paramiko.ssh_exception import SSHException
import yaml


def configure_net_devices(device_params, commands):
    try:
        with Netmiko(**device_params) as ssh:
            ssh.enable()
            cmd_output = ssh.send_config_set(commands)
        return cmd_output
    except (NetmikoBaseException, SSHException) as error:
        print(error)


if __name__ == "__main__":
    with open("devices.yaml") as f:
        device_list = yaml.safe_load(f)
    for device in device_list:
        result = configure_net_devices(device, "logging 10.1.1.1")
        pprint(result, width=120)
