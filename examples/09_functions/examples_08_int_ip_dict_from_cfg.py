from pprint import pprint


def get_intf_ip_dict_from_cfg(filename):
    intf_ip_dict = {}
    with open(filename) as f:
        for line in f:
            if line.startswith("interface"):
                intf = line.split()[-1]
                intf_ip_dict[intf] = None
            elif line.startswith(" ip address"):
                ip = line.split()[-2]
                intf_ip_dict[intf] = ip
    return intf_ip_dict


result = get_intf_ip_dict_from_cfg("configs/config_r1.txt")
pprint(result)
