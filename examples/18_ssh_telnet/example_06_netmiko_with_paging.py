import re
from pprint import pprint
from netmiko import Netmiko, NetmikoBaseException
import yaml


def send_show_command(device_params, command):
    with Netmiko(**device_params) as ssh:
        ssh.enable()
        prompt = ssh.find_prompt()
        ssh.send_command("terminal length 10")
        ssh.write_channel(f"{command}\n")
        output = ""
        while True:
            try:
                page = ssh.read_until_pattern(f"More|{prompt}", read_timeout=5)
            except NetmikoBaseException:
                break
            else:
                output += page
                print(page)
                print("="*30)
                if "More" in page:
                    ssh.write_channel(" ")
                elif prompt in output:
                    break
        output = re.sub(r" +--More-- +\x08+ +\x08+", "", output)
    return output


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    out = send_show_command(devices[0], "sh run")
    pprint(out)
    # with open("output.txt", "w") as f:
    #     f.write(out)
