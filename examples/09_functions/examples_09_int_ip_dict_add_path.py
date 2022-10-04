from pprint import pprint


def get_intf_ip_dict_from_cfg(filename):
    intf_ip_dict = {}
    with open(filename) as f:
        for line in f:
            if line.startswith("interface"):
                intf = line.split()[-1]
                # intf_ip_dict[intf] = None
            elif line.startswith(" ip address"):
                ip = line.split()[-2]
                intf_ip_dict[intf] = ip
    return intf_ip_dict


def get_host_intf_ip_dict(config_list):
    host_intf = {}
    for file in config_list:
        host = file.split("_")[-1].split(".")[0]
        result_dict = get_intf_ip_dict_from_cfg(file)
        host_intf[host] = result_dict
    return host_intf



path = "/home/vagrant/repos/pyneng-14/pyneng-course-examples/examples/09_functions"
cfg_list = [
    "configs/config_r1.txt",
    "configs/config_r2.txt",
    "configs/config_r3.txt",
    "configs/config_sw1.txt",
]
cfg_list_full = [f"{path}/{f}" for f in cfg_list]
pprint(cfg_list_full)
result = get_host_intf_ip_dict(cfg_list)
pprint(result)
