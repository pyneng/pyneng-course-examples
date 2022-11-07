from pprint import pprint
from netmiko import (
    Netmiko,
    NetmikoBaseException,
    ReadException
)
from paramiko.ssh_exception import SSHException


common_params = {
    "device_type": "cisco_ios",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
    # "port": "22222",
    "conn_timeout": 2,
    "timeout": 5
}


def get_show_output(device_params, show):
    try:
        with Netmiko(**device_params) as ssh:
            ssh.enable()
            show_output = ssh.send_command(show)
            show_output = ssh.send_command("ping 8.8.8.8 repeat 6")
            return show_output
    except ReadException as error:
        print(f"Read error {error}")
    except (NetmikoBaseException, SSHException) as error:
        print(error)



if __name__ == "__main__":
    device_list = ["192.168.100.1", "192.168.100.11", "192.168.100.2", "192.168.100.3"]
    for ip in device_list:
        device = common_params.copy()
        device["host"] = ip
        if ip == "192.168.100.2":
            device["password"] = "wrong"
        print(get_show_output(device, "sh run | i hostname"))
