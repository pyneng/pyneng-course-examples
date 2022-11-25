from pprint import pprint

from textfsm import clitable
from netmiko import Netmiko
import yaml


def get_show_output(device_params, show):
    with Netmiko(**device_params) as ssh:
        ssh.enable()
        out = ssh.send_command(show)
        return out


def parse_output(output, command):
    cli = clitable.CliTable("index", "templates")
    cli.ParseCmd(output, {"Command": command})

    data = [list(row) for row in cli]
    header = list(cli.header)

    return [header, *data]



if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        device_list = yaml.safe_load(f)
    for device in device_list:
        result = get_show_output(device, command)
        pprint(result, width=150)
        # pprint(parse_output(result, command))
