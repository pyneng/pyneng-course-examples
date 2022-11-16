from pprint import pprint
import socket
from concurrent.futures import ThreadPoolExecutor
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
            return {device: output}
    except (
        NetmikoAuthenticationException,
        socket.timeout,
        NetmikoTimeoutException,
    ) as error:
        logging.info(f"Ошибка {error} при подключении к {device}")
    except NetmikoBaseException as error:
        logging.info(f"Ошибка netmiko {error} при подключении к {device}")
    return {device: None}


with open("devices.yaml") as f:
    devices = yaml.safe_load(f)

cmd = "sh run | i hostname"

with ThreadPoolExecutor(max_workers=5) as ex:  # create threads
    ip_out_dict = {}
    result = ex.map(send_show, devices, repeat(cmd))
    for result_dict in result:
        if result_dict:
            ip_out_dict.update(result_dict)
    pprint(ip_out_dict)
