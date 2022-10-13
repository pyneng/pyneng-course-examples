import subprocess
from rich import print as rprint


def ping_ip(ip):
    rprint(f"[yellow]Пингую[/yellow] IP {ip}...")
    result = subprocess.run(["ping", "-c", "1", ip], capture_output=True)
    if result.returncode == 0:
        return True
    else:
        return False


ip_list = ["8.8.8.8", "192.168.100.1", "10.1.1.1"]

for ip in ip_list:
    status = ping_ip(ip)
    if status:
        rprint(f"[green]{ip=} {status=}")
    else:
        rprint(f"[red]{ip=} {status=}")
