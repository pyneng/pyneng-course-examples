from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
import logging
from pprint import pprint
import re

from netmiko import Netmiko, NetmikoBaseException
from paramiko.ssh_exception import SSHException
import yaml


logging.getLogger("paramiko").setLevel(logging.WARNING)
logging.getLogger("netmiko").setLevel(logging.WARNING)

logging.basicConfig(
    format="{asctime} {levelname} {message}",
    datefmt="%H:%M:%S",
    style="{",
    level=logging.DEBUG,
)


def get_show_output(device_params, show):
    try:
        with Netmiko(**device_params) as ssh:
            ssh.enable()
            out = ssh.send_command(show)
            return out
    except (NetmikoBaseException, SSHException) as error:
        print(error)


def send_show_to_devices(device_list, command, threads=5):
    host_output_dict = {}
    with ThreadPoolExecutor(max_workers=threads) as ex:
        all_results = ex.map(get_show_output, device_list, repeat(command))
        for device, out in zip(device_list, all_results):
            host = device["host"]
            host_output_dict[host] = out
    return host_output_dict


def parse_sh_ip_int_br(output):
    regex = re.compile(
        r"(\S+) +(\S+) +\w+ \w+ +(administratively down|up|down) +(up|down)"
    )
    sh_ip_int_br = [m.groups() for m in regex.finditer(output)]
    return sh_ip_int_br


def parse_show_output(parse_function, host_output_dict):
    host_parsed_dict = {}
    for host, output in host_output_dict.items():
        if output:
            host_parsed_dict[host] = parse_function(output)
    return host_parsed_dict



if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    ip_out_dict = send_show_to_devices(devices, "sh ip int br")
    pprint(ip_out_dict)
    ip_parsed_dict = parse_show_output(parse_sh_ip_int_br, ip_out_dict)
    pprint(ip_parsed_dict, width=120)
