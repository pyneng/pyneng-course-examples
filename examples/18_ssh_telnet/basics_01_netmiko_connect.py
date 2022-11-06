from pprint import pprint
from netmiko import Netmiko


device = {
    "device_type": "cisco_ios",
    "host": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
}

# r1 = Netmiko(host="192.168.100.1", username="cisco", password="cisco", secret="cisco", device_type="cisco_ios")
with Netmiko(host="192.168.100.1", username="cisco", password="cisco",
             secret="cisco", device_type="cisco_ios") as r1:
    r1.enable()
    out = r1.send_command("sh clock")
    print(out)


with Netmiko(**device) as r1:
    r1.enable()
    out = r1.send_command("sh clock")
    print(out)
