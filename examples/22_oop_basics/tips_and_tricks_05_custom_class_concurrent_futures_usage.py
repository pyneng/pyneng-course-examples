from pprint import pprint
from concurrent.futures import ThreadPoolExecutor
import logging
from itertools import repeat

import yaml
from tips_and_tricks_05_custom_class_concurrent_futures import CiscoSSH

logging.getLogger("paramiko").setLevel(logging.WARNING)

logging.basicConfig(
    format="{threadName} {asctime} {name} {levelname} {message}",
    datefmt="%H:%M:%S",
    style="{",
    level=logging.DEBUG,
)


def send_show(device_dict, command):
    host = device_dict["host"]
    logging.info(f">>> Подключаюсь к {host}")
    conn = CiscoSSH(**device_dict)
    logging.debug(f"Отправляю команду {command} на {host}")
    output = conn.send_show(command)
    logging.info(f"<<< Получили вывод {host}")
    conn.close()
    return output


def send_show_to_devices(device_list, command, threads=5):
    host_output_dict = {}
    with ThreadPoolExecutor(max_workers=threads) as ex:
        all_results = ex.map(send_show, device_list, repeat(command))
        for device, out in zip(device_list, all_results):
            host = device["host"]
            host_output_dict[host] = out
    return host_output_dict


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    data = send_show_to_devices(devices, "sh clock")
    pprint(data)

