import subprocess
from concurrent.futures import ThreadPoolExecutor
from rich import print as rprint


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


ip_list = ["8.8.8.8", "192.168.100.22", "192.168.100.1"]
with ThreadPoolExecutor(max_workers=3) as ex:
    result = ex.map(ping_ip, ip_list)
    for ip, status in zip(ip_list, result):
        if status:
            rprint(f"[green]Пингуется {ip}")
        else:
            rprint(f"[red]Не пингуется {ip}")
