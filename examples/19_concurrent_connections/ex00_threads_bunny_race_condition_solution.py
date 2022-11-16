from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
import random
import time
from threading import Lock

account = {"balance": 1000}

def get_bunny(id, lock, amount=1):
    print(f"get_bunny {id} {amount=}")
    time.sleep(random.random())
    with lock:
        balance = account["balance"]
        if amount < balance:
            new_balance = balance - amount
            time.sleep(random.random())
            account["balance"] = new_balance
            print(f"get_bunny {id} done")
            return True
        else:
            return False


def count_bunnies(bunny_total, limit_threads=100):
    lock = Lock()
    with ThreadPoolExecutor(max_workers=limit_threads) as executor:
        results = executor.map(get_bunny, range(bunny_total), repeat(lock))
        for output in results:
            pass


if __name__ == "__main__":
    count_bunnies(bunny_total=200)
    print(account)
