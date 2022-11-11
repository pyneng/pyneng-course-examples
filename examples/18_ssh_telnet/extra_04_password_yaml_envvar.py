from pprint import pprint
from netmiko import Netmiko, NetmikoBaseException
from paramiko.ssh_exception import SSHException
from pyaml_env import parse_config



def get_show_output(device_params, show):
    try:
        with Netmiko(**device_params) as ssh:
            ssh.enable()
            out = ssh.send_command(show)
            return out
    except (NetmikoBaseException, SSHException) as error:
        print(error)


if __name__ == "__main__":
    device_list = parse_config('devices_envvar.yaml')
    pprint(device_list)
    for device in device_list:
        result = get_show_output(device, "sh ip int br | i up.*up")
        pprint(result, width=120)
