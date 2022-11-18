from concurrent.futures import ThreadPoolExecutor
import random
from itertools import repeat
import time

account = {"balance": 1000}

def get_bunny(id, amount=1):
    print(f"get_bunny {id} {amount=}")
    time.sleep(random.random() * 4)
    balance = account["balance"]
    if amount < balance:
        time.sleep(random.random())
        new_balance = balance - amount
        time.sleep(random.random())
        account["balance"] = new_balance
        # print(f"get_bunny {id} done")
        return True
    else:
        return False


def count_bunnies(bunny_total, limit_threads=20):
    with ThreadPoolExecutor(max_workers=limit_threads) as executor:
        results = executor.map(get_bunny, range(bunny_total))
        for output in results:
            pass


if __name__ == "__main__":
    count_bunnies(bunny_total=60)
    print(account)
