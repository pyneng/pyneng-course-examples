from concurrent.futures import ThreadPoolExecutor
import time
import logging
import random
from itertools import repeat


logging.basicConfig(
    format="{threadName} {asctime} {name} {levelname} {message}",
    datefmt="%H:%M:%S",
    style="{",
    level=logging.DEBUG,
)

def thing(device):
    if device == 13:
        raise ValueError


def connect(device, command):
    logging.info(f">>> Подключаюсь {device}")
    time.sleep(random.random())
    logging.info(f"Отправляю команду {device} {command}")
    try:
        thing(device)
    except ValueError:
        return None
    time.sleep(10)
    time.sleep(random.random())
    logging.info(f"<<< Получили вывод {device}")
    return f"{device} {command}"


devices = range(1, 31)
cmd = "sh clock"

with ThreadPoolExecutor(max_workers=10) as ex: # create threads
    result = ex.map(connect, devices, repeat(cmd))
    for i in result:
        print(f"result = {i}")
# wait threads

