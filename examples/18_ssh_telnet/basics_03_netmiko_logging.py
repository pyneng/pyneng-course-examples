import logging
import netmiko


# logging.getLogger("paramiko").setLevel(logging.WARNING)

logging.basicConfig(
    format="{asctime} - {name} - {levelname} - {message}",
    datefmt="%H:%M:%S",
    style="{",
    level=logging.INFO,
)


def send_show(device, show):
    host = device["host"]
    logging.info(f"===> Connection: {host}")

    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(show)
        logging.info(f"<=== Received:   {host}")
    return result


device = {
    "device_type": "cisco_ios",
    "host": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
}

if __name__ == "__main__":
    print(send_show(device, "sh clock"))
