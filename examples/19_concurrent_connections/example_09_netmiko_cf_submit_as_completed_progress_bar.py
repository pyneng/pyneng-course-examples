from pprint import pprint
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging
import time
import random

import yaml
from netmiko import Netmiko, NetmikoBaseException
from rich.progress import track

logging.getLogger("paramiko").setLevel(logging.WARNING)
logging.getLogger("netmiko").setLevel(logging.WARNING)

logging.basicConfig(
    filename="log_ex09.log",
    format="{threadName} {asctime} {name} {levelname} {message}",
    style="{",
    level=logging.DEBUG,
)


def send_show(device_dict, command):
    host = device_dict["host"]
    logging.info(f">>> Подключаюсь к {host}")
    with Netmiko(**device_dict) as conn:
        time.sleep(random.random() * 2)
        conn.enable()
        logging.debug(f"Отправляю команду {command} на {host}")
        output = conn.send_command(command)
        logging.info(f"<<< Получили вывод {host}")
        return host, output


def send_show_to_devices(device_list, command, threads=5):
    host_output_dict = {}
    with ThreadPoolExecutor(max_workers=threads) as ex:
        task_queue = []
        for device in device_list:
            task = ex.submit(send_show, device, command)
            task_queue.append(task)
        # task_queue = [ex.submit(send_show, device, command) for device in device_list]
        for task in track(as_completed(task_queue), total=len(device_list)):
            host, output = task.result()
            host_output_dict[host] = output
    return host_output_dict


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    cmd = "sh run | i hostname"
    pprint(send_show_to_devices(devices, cmd), sort_dicts=False)
