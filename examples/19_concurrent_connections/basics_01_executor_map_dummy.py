from pprint import pprint
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


def connect(device, command):
    logging.info(f">>> Подключаюсь {device}")
    time.sleep(random.random() * 3)
    #logging.info(f"Отправляю команду {device} {command}")
    #time.sleep(random.random() * 3)
    if device == 11:
        raise ValueError
    logging.info(f"<<< Получили вывод {device}")
    return f"{device} {command}"


devices = range(1, 21)
command = "sh clock"

with ThreadPoolExecutor(max_workers=5) as ex: # create pool
    result = ex.map(connect, devices, repeat(command)) # create tasks
    for i in result:
        pprint(i)
# wait threads
