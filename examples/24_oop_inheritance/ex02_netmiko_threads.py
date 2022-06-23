from concurrent.futures import ThreadPoolExecutor
import re
from pprint import pprint
import time
import random
from itertools import repeat
from datetime import datetime
import yaml

from cisco_telnet import CiscoTelnet


def send_show_command(device, show):
    with CiscoTelnet(**device) as ssh:
        output = ssh.send_command(show)
        return output


def send_show_to_devices(devices, show):
    result_dict = {}
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(send_show_command, devices, repeat(show))
        for dev, output in zip(devices, results):
            host = dev['ip']
            result_dict[host] = output
    print("### Все потоки отработали")
    return result_dict


if __name__ == "__main__":
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    r = send_show_to_devices(devices, "sh int desc")
    pprint(r)
