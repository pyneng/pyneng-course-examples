from pprint import pprint
from netmiko import Netmiko, NetmikoBaseException
from paramiko.ssh_exception import SSHException
import yaml
from rich import print as rprint


def configure_net_devices(device_params, commands, check_cmd=None, check_str=None):
    try:
        with Netmiko(**device_params) as ssh:
            ssh.enable()
            cmd_output = ssh.send_config_set(commands)
            if check_cmd and check_str:
                check_output = ssh.send_command(check_cmd)
                if check_str in check_output:
                    rprint("[green]Настройка прошла успешно")
                else:
                    rprint("[red]Настройка не прошла проверку")
        return cmd_output
    except (NetmikoBaseException, SSHException) as error:
        print(error)


if __name__ == "__main__":
    with open("devices.yaml") as f:
        device_list = yaml.safe_load(f)
    r1 = device_list[0]
    result = configure_net_devices(
        r1, ["router ospf 1", "network 0.0.0.0 255.255.255.255 area 0"],
        check_cmd="sh ip ospf", check_str="Ring Process"
    )
    pprint(result)
