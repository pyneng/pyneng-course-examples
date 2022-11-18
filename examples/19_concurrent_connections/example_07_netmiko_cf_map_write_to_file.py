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
    host = device_dict["host"]
    logging.info(f">>> Подключаюсь к {host}")
    with Netmiko(**device_dict) as conn:
        conn.enable()
        logging.debug(f"Отправляю команду {command} на {host}")
        output = conn.send_command(command)
        logging.info(f"<<< Получили вывод {host}")
        return output


def send_show_to_devices(
    device_list, command, output_file="results.txt", threads=5
):
    logging.info(f"Начинаем подключаться...")
    host_output_dict = {}
    with ThreadPoolExecutor(max_workers=threads) as ex:
        all_results = ex.map(send_show, device_list, repeat(command))
        logging.info(f"Поставили все задачи...")
        for device, out in zip(device_list, all_results):
            host = device["host"]
            host_output_dict[host] = out
    return host_output_dict


def send_show_to_devices_2(
    device_list, command, output_file="results.txt", threads=5
):
    logging.info(f"Начинаем подключаться...")
    host_output_dict = {}
    with ThreadPoolExecutor(max_workers=threads) as ex:
        all_results = ex.map(send_show, device_list, repeat(command))
        logging.info(f"Поставили все задачи...")
        with open(output_file, "w") as f:
            for device, out in zip(device_list, all_results):
                host = device["host"]
                f.write(f"\n{host}\n")
                f.write(out)


def send_show_to_devices_3(device_list, command, threads=5):
    logging.info(f"Начинаем подключаться...")
    host_output_dict = {}
    with ThreadPoolExecutor(max_workers=threads) as ex:
        all_results = ex.map(send_show, device_list, repeat(command))
        logging.info(f"Поставили все задачи...")
        for device, out in zip(device_list, all_results):
            host = device["host"]
            file = (
                f"{host.replace('.', '_')}_{command.replace(' ', '_')}.txt"
            )
            with open(file, "w") as f:
                f.write(out)



if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    data = send_show_to_devices_3(devices, "sh ip int br")
    pprint(data, width=120)


