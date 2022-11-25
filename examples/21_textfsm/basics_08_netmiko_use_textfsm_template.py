from pprint import pprint

from netmiko import Netmiko
import yaml


def get_show_output(device_params, show, template_file):
    with Netmiko(**device_params) as ssh:
        ssh.enable()
        out = ssh.send_command(show, use_textfsm=True, textfsm_template=template_file)
        return out


if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        device_list = yaml.safe_load(f)
    for device in device_list:
        result = get_show_output(device, command, template_file="templates/sh_ip_int_br.txt")
        pprint(result, width=150)
