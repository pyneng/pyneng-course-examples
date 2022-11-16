from pprint import pprint
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import logging
import random
from itertools import repeat

import yaml
from netmiko import (
    Netmiko,
    NetmikoAuthenticationException,
    NetmikoBaseException,
    NetmikoTimeoutException,
)

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
            return device, output
    except (
        NetmikoAuthenticationException,
        socket.timeout,
        NetmikoTimeoutException,
    ) as error:
        logging.info(f"Ошибка {error} при подключении к {device}")
        return device, None
    except NetmikoBaseException as error:
        logging.info(f"Ошибка netmiko {error} при подключении к {device}")
        return device, None



def send_cmd_to_all(devices, command, threads=10):
    ip_out_dict = {}
    errors_on_devices = []
    with ThreadPoolExecutor(max_workers=threads) as ex:  # create threads
        task_queue = [ex.submit(send_show, dev, command=command)
                      for dev in devices]
        for future in as_completed(task_queue):
            ip, output = future.result()
            if output:
                ip_out_dict[ip] = output
            else:
                errors_on_devices.append(ip)
    pprint(errors_on_devices)
    return ip_out_dict


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    cmd = "sh run | i hostname"
    pprint(send_cmd_to_all(devices, cmd), sort_dicts=False)
