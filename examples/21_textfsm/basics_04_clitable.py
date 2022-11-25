from pprint import pprint
from textfsm import clitable


with open("output/sh_ip_int_br.txt") as f:
	output = f.read()


cli = clitable.CliTable("index", "templates")
cli.ParseCmd(output, {"Command": "sh ip int br"})

data = [list(row) for row in cli]
header = list(cli.header)

pprint(data)
