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
    "timeout": 5
}




if __name__ == "__main__":
    device_list = ["192.168.100.1", "192.168.100.11", "192.168.100.2", "192.168.100.3"]
