from pprint import pprint
import telnetlib
from concurrent.futures import ThreadPoolExecutor
import yaml


def get_cisco_show_output(host, username, password, enable_pass, command):
    with telnetlib.Telnet(host) as t:
        t.read_until(b'Username:')
        t.write(f"{username}\n".encode("utf-8"))
        t.read_until(b'Password')
        t.write(f"{password}\n".encode("utf-8"))
        t.read_until(b'>')

        t.write(b"enable\n")
        t.read_until(b'Password')
        t.write(f"{enable_pass}\n".encode("utf-8"))
        t.read_until(b'#')
        t.write(b"terminal length 0\n")
        boutput = t.read_until(b'#', timeout=5)

        t.write(f"{command}\n".encode("utf-8"))
        boutput = t.read_until(b'#', timeout=5)
        output = boutput.decode("utf-8").replace("\r\n", "\n")
        return output


def send_show_to_devices(device_list, command, threads=5):
    host_output_dict = {}
    with ThreadPoolExecutor(max_workers=threads) as ex:
        task_queue = []
        for device in device_list:
            task = ex.submit(get_cisco_show_output, **device, command=command)
            task_queue.append(task)
        # task_queue = [ex.submit(send_show, device, command) for device in device_list]
        for device, task in zip(device_list, task_queue):
            host = device["host"]
            output = task.result()
            host_output_dict[host] = output
    return host_output_dict


if __name__ == "__main__":
    with open("devices_telnetlib.yaml") as f:
        devices = yaml.safe_load(f)
    cmd = "sh run | i hostname"
    pprint(send_show_to_devices(devices, cmd))
