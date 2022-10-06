from pprint import pprint
from typing import List, Dict


def parse_sh_ip_int_br(filename: str) -> List[List[str]]:
    result_list = []
    with open(filename) as f:
        for line in f:
            if "up" in line or "down" in line:
                intf, ip, *_, status = line.split()
                result_list.append([intf, ip, status])
    return result_list


def count_ports_2(sh_ip_int_br_list: List[List[str]]) -> Dict[str, int]:
    result_dict = {
        "up": 0,
        "down": 0,
    }
    for intf, ip, status in sh_ip_int_br_list:
        if status == "up":
            result_dict["up"] += 1
        elif status == "down":
            result_dict["down"] += 1
    return result_dict


data = parse_sh_ip_int_br("show_output/sh_ip_int_br.txt")
ports = count_ports_2(data)
pprint(data)
pprint(ports)
