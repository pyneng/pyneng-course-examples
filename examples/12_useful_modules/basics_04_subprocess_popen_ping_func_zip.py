import subprocess
from  pprint import pprint


def ping_ip_list(ip_list):
    process_list = []
    for ip in ip_list:
        print(f"Пингую IP {ip}...")
        process = subprocess.Popen(
            ["ping", "-c", "3", ip],
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
        )
        process_list.append(process)

    status_list = []
    for pr in process_list:
        returncode = pr.wait()
        ip = pr.args[-1]
        if returncode == 0:
            status_list.append(True)
        else:
            status_list.append(False)
    result = dict(zip(ip_list, status_list))
    return result



ip_list = ["8.8.8.8", "10.1.1.1", "192.168.100.1", "10.2.2.2"]

result = ping_ip_list(ip_list)
pprint(result)
