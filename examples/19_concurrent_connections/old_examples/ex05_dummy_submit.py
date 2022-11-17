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

def connect1(device, command):
    logging.info(f">>> Подключаюсь {device}")
    time.sleep(random.random())
    logging.info(f"<<< Получили вывод {device}")
    return f"{device} {command}"

def connect2(device, command):
    logging.info(f">>> Подключаюсь {device}")
    time.sleep(random.random())
    logging.info(f"<<< Получили вывод {device}")
    return f"{device} {command}"

def connect3(device, command):
    logging.info(f">>> Подключаюсь {device}")
    time.sleep(random.random())
    logging.info(f"<<< Получили вывод {device}")
    raise ValueError
    return f"{device} {command}"


devices = range(1, 31)
r1, r2, r3 = 1, 2, 3
cmd = "sh clock"

with ThreadPoolExecutor(max_workers=10) as ex: # create threads
    f1 = ex.submit(connect1, r1, cmd)
    f2 = ex.submit(connect2, r2, cmd)
    f3 = ex.submit(connect3, r3, cmd)
    print(f1, f2, f3, sep='\n')
    for fut in (f1, f2, f3):
        try:
            result = fut.result()
            print(f"{result=}")
        except ValueError:
            print(fut)


# wait threads

