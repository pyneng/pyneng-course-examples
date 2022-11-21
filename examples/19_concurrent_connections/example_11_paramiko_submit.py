from pprint import pprint
from concurrent.futures import ThreadPoolExecutor
import time

import yaml
import paramiko


def cisco_get_show_output(
    host, username, password, enable_pass, command, pause=0.5, max_read=100000
):
    with paramiko.SSHClient() as client:
        client.load_system_host_keys()
        client.connect(
            hostname=host,
            username=username,
            password=password,
            look_for_keys=False,
            allow_agent=False,
        )
        ssh = client.invoke_shell()
        ssh.send("enable\n")
        time.sleep(pause)
        ssh.send(f"{enable_pass}\n")
        time.sleep(pause)
        ssh.send("terminal length 0\n")
        time.sleep(pause)
        ssh.recv(max_read)

        ssh.send(f"{command}\n")
        time.sleep(pause * 4)
        output = ssh.recv(max_read)
        return output.decode("utf-8").replace("\r\n", "\n")


def send_show_to_devices(device_list, command, threads=5):
    host_output_dict = {}
    with ThreadPoolExecutor(max_workers=threads) as ex:
        task_queue = []
        for dev in device_list:
            task = ex.submit(cisco_get_show_output, **dev, command=command)
            task_queue.append(task)
        for dev, task in zip(device_list, task_queue):
            host = dev["host"]
            out = task.result()
            host_output_dict[host] = out
    return host_output_dict


if __name__ == "__main__":
    with open("devices_telnetlib.yaml") as f:
        devices = yaml.safe_load(f)
    cmd = "sh run | i hostname"
    pprint(send_show_to_devices(devices, cmd))
