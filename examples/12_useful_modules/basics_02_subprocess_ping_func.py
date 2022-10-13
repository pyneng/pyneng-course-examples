import subprocess


def ping_ip(ip):
    print(f"Пингую IP {ip}...")
    result = subprocess.run(["ping", "-c", "3", ip], capture_output=True)
    if result.returncode == 0:
        return True
    else:
        return False


ip_list = ["8.8.8.8", "10.1.1.1", "192.168.100.1"]

for ip in ip_list:
    status = ping_ip(ip)
    print(f"{ip=} {status=}")
