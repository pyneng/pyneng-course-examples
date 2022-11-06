from pprint import pprint
from netmiko import (
    Netmiko,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
    ReadTimeout,
)


common_params = {
    "device_type": "cisco_ios",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
    # "port": "22222",
    "conn_timeout": 2,
}


def get_show_output(device, command):
    try:
        with Netmiko(**device) as r1:
            r1.enable()
            # out = r1.send_command("ping 8.8.8.8 repeat 6")
            out = r1.send_command(command)
            return out
    except (
        NetmikoTimeoutException, # wrong ip/port
        NetmikoAuthenticationException, # username/password
        ReadTimeout, # wrong enable/prompt timeout
    ) as error:
        print(error)


if __name__ == "__main__":
    device_list = ["192.168.100.1", "192.168.100.2", "192.168.100.3"]
    for ip in device_list:
        device = common_params.copy()
        device["host"] = ip
        print(get_show_output(device, "sh run | i hostname"))
