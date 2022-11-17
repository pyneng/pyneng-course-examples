from pprint import pprint
from concurrent.futures import ThreadPoolExecutor
import logging
from itertools import repeat

import yaml
from netmiko import Netmiko, NetmikoBaseException

logging.getLogger("paramiko").setLevel(logging.WARNING)
logging.getLogger("netmiko").setLevel(logging.WARNING)

logging.basicConfig(
    format="{threadName} {asctime} {name} {levelname} {message}",
    datefmt="%H:%M:%S",
    style="{",
    level=logging.DEBUG,
)


def send_show(device_dict, command):
    device = device_dict["host"]
    logging.info(f">>> Подключаюсь {device}")
    try:
        with Netmiko(**device_dict) as conn:
            conn.enable()
            logging.info(f"Отправляю команду {device} {command}")
            output = conn.send_command(command)
            logging.info(f"<<< Получили вывод {device}")
            return output
    except (NetmikoBaseException, SSHException) as error:
        print(error)


def send_cmd_to_all(devices, command, threads=10):
    ip_out_dict = {}
    with ThreadPoolExecutor(max_workers=threads) as ex:  # create threads
        result = ex.map(send_show, devices, repeat(command))
        for device, output in zip(devices, result):
            ip_out_dict[device["host"]] = output
    return ip_out_dict


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    cmd = "sh run | i hostname"
    pprint(send_cmd_to_all(devices, cmd))
