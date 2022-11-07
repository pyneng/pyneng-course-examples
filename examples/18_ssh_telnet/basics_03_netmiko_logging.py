import logging
import netmiko


logging.getLogger("paramiko").setLevel(logging.INFO)
logging.getLogger("netmiko").setLevel(logging.INFO)

logging.basicConfig(
    format="{asctime} - {name} - {levelname} - {message}",
    datefmt="%H:%M:%S",
    style="{",
    level=logging.DEBUG,
)


def send_show(device, show):
    host = device["host"]
    logging.info(f">>>> Connection {host}")
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(show)
        logging.debug(f"<<<< Received {host}\n\n{result}")
    return result


device = {
    "device_type": "cisco_ios",
    "host": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
}

if __name__ == "__main__":
    send_show(device, "sh ip int br")
