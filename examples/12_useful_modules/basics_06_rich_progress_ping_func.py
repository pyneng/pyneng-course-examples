import subprocess
from rich.progress import track

def ping_ip(ip):
    result = subprocess.run(["ping", "-c", "3", ip], capture_output=True)
    if result.returncode == 0:
        return True
    else:
        return False


ip_list = ["8.8.8.8", "192.168.100.1", "192.168.100.2", "192.168.100.3"]

for ip in track(ip_list, description="Пингуем IP"):
    status = ping_ip(ip)
