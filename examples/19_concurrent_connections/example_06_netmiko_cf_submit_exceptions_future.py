from pprint import pprint
from concurrent.futures import ThreadPoolExecutor
import logging

import yaml
from netmiko import Netmiko, NetmikoBaseException
from paramiko.ssh_exception import SSHException

logging.getLogger("paramiko").setLevel(logging.WARNING)
logging.getLogger("netmiko").setLevel(logging.WARNING)

logging.basicConfig(
    format="{threadName} {asctime} {name} {levelname} {message}",
    datefmt="%H:%M:%S",
    style="{",
    level=logging.INFO,
)


def send_show(device_dict, command):
    device = device_dict["host"]
    logging.info(f">>> Подключаюсь {device}")
    with Netmiko(**device_dict) as conn:
        conn.enable()
        logging.info(f"Отправляю команду {device} {command}")
        output = conn.send_command(command)
        logging.info(f"<<< Получили вывод {device}")
        return output


def send_show_to_devices(device_list, command, threads=5):
    host_output_dict = {}
    with ThreadPoolExecutor(max_workers=threads) as ex:
        task_queue = []
        for device in device_list:
            task = ex.submit(send_show, device, command)
            task_queue.append(task)
        # task_queue = [ex.submit(send_show, device, command) for device in device_list]
        for device, task in zip(device_list, task_queue):
            host = device["host"]
            exc = task.exception()
            if exc:
                host_output_dict[host] = exc
            else:
                output = task.result()
                host_output_dict[host] = output
    return host_output_dict


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    cmd = "sh run | i hostname"
    pprint(send_show_to_devices(devices, cmd))
