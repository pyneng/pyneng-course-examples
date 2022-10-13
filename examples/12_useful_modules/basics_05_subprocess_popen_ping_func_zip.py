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

    result = {}
    for ip, pr in zip(ip_list, process_list):
        returncode = pr.wait()
        if returncode == 0:
            result[ip] = True
        else:
            result[ip] = False
    return result



ip_list = ["8.8.8.8", "10.1.1.1", "192.168.100.1", "10.2.2.2"]

result = ping_ip_list(ip_list)
pprint(result)
