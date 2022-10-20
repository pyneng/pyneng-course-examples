from pprint import pprint
import re



def parse_mac_address_table(filename):
    result = []
    regex = r"(\d+) +(\S+) +\w+ +(\S+)"
    with open(filename) as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                result.append(match.groups())
    return result

filename = "show_output/sh_mac_address.txt"
list_result = parse_mac_address_table(filename)
pprint(list_result)
