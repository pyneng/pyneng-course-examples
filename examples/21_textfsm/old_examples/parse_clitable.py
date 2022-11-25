import yaml
from pprint import pprint
import netmiko
from textfsm import clitable
import textfsm


def parse_output_textfsm(
    output,
    attributes_dict,
    pth="/home/vagrant/repos/pyneng-11/pyneng-online-11-jun-aug-2021/examples/21_textfsm/templates",
    index="index",
):
    cli = clitable.CliTable(index, pth)  # clitable
    cli.ParseCmd(output, attributes_dict)  # clitable
    data = [list(item) for item in cli]  # clitable
    return data


if __name__ == "__main__":
    cmd = "sh mac"
    with open("output/sh_mac.txt") as f:
        output = f.read()
    pprint(parse_output_textfsm(output, {"Command": cmd}))
