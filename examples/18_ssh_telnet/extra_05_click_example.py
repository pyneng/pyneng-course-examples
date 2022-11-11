import click
from netmiko import ConnectHandler
import yaml


def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


def send_command_to_cisco_devices(device_list, command):
    result = {}
    for device in device_list:
        ip = device["host"]
        result[ip] = send_show_command(device, command)
    return result


@click.command()
@click.argument("command")
@click.option("--yaml-params", "-y", type=click.File("r"), required=True)
@click.option("--password", "-p", envvar="SSH_PASSWORD", prompt=True, hide_input=True)
@click.option("--secret", "-s", envvar="NET_SECRET", prompt=True, hide_input=True)
def main(command, yaml_params, password, secret):
    devices = yaml.safe_load(yaml_params)
    device_list = []
    for dev in devices:
        params = {
            **dev,
            "password": password,
            "secret": secret,
        }
        device_list.append(params)

    result_dict = send_command_to_cisco_devices(device_list, command)
    for ip, output in result_dict.items():
        print(ip.center(30, "="))
        print(output)


if __name__ == "__main__":
    main()
