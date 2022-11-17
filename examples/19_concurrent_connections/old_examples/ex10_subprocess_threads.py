import subprocess
from concurrent.futures import ThreadPoolExecutor

def ping_ip(ip):
    p = subprocess.run(
        ["ping", "-c", "3", "-n", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if p.returncode == 0:
        return True
    else:
        return False


def ping_ip_addresses(ip_list, threads=5):
    reachable = []
    unreachable = []
    with ThreadPoolExecutor(max_workers=threads) as ex:  # create threads
        result = ex.map(ping_ip, ip_list)
        for ip, status in zip(ip_list, result):
            if status:
                reachable.append(ip)
            else:
                unreachable.append(ip)
    return reachable, unreachable


if __name__ == "__main__":
    print(ping_ip_addresses(["8.8.8.8", "192.168.100.22", "192.168.100.1"]))
