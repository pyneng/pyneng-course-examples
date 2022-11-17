from pprint import pprint
from concurrent.futures import ThreadPoolExecutor, as_completed
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
    logging.info(f"<<< Получили вывод {device}")
    return f"{device} {command}"


devices = range(1, 21)
command = "sh clock"

with ThreadPoolExecutor(max_workers=5) as ex: # create pool
    task_queue = []
    for dev in devices:
        task = ex.submit(connect, dev, command)
        task_queue.append(task)
    # task_queue = [ex.submit(connect, dev, command) for dev in devices]
    for t in as_completed(task_queue):
        pprint(t.result()) # wait for result

# wait threads
