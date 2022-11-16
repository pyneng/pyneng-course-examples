from concurrent.futures import ThreadPoolExecutor
import time
import logging
import random
from itertools import repeat
from pprint import pprint


logging.basicConfig(
    format="{threadName} {asctime} {name} {levelname} {message}",
    datefmt="%H:%M:%S",
    style="{",
    level=logging.DEBUG,
)

def connect(device, command):
    logging.info(f">>> Подключаюсь {device}")
    time.sleep(random.random())
    logging.info(f"Отправляю команду {device} {command}")
    time.sleep(random.random())
    logging.info(f"<<< Получили вывод {device}")
    return f"{device} {command}"


devices = range(1, 31)
cmd = "sh clock"

with ThreadPoolExecutor(max_workers=10) as ex: # create threads
    future_list = []
    for dev in devices:
        future = ex.submit(connect, dev, cmd)
        future_list.append(future)
    # future_list = [ex.submit(connect, dev, cmd) for dev in devices]
    pprint(future_list)
    for fut in future_list:
        result = fut.result()
        print(f"{result=}")


# wait threads

