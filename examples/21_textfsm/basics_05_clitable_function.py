from pprint import pprint
from textfsm import clitable


def parse_output(output, command):
    cli = clitable.CliTable("index", "templates")
    cli.ParseCmd(output, {"Command": command})

    data = [list(row) for row in cli]
    header = list(cli.header)

    return [header, *data]


if __name__ == "__main__":
    with open("output/sh_ip_int_br.txt") as f:
        output = f.read()
    pprint(parse_output(output, "sh ip int br"))
