from rich.tree import Tree
from rich import print

vrf = {
    "dmz": {
        "network": [
            "10.1.9.0/24",
            "10.1.10.0/27",
            "10.1.11.0/26",
            "10.1.12.0/24",
            "10.1.14.0/23",
            "10.1.16.0/23",
            "10.42.96.224/27",
            "10.31.31.48/30",
            "10.31.41.8/29",
            "10.31.41.168/29",
            "10.31.41.192/29",
            "10.42.96.16/29",
            "10.255.191.0/25",
        ]
    },
    "internet": {
        "network": [
            "10.1.9.0/24",
            "10.1.10.0/27",
            "10.1.11.0/26",
            "10.1.12.0/24",
            "10.31.41.184/29",
            "10.16.8.88/29",
            "10.255.191.0/25",
        ]
    },
    "vpn": {
        "network": [
            "10.1.9.0/24",
            "10.1.10.0/27",
            "10.255.240.0/21",
            "10.255.247.128/25",
            "10.42.96.224/27",
            "10.42.97.64/29",
            "10.42.97.72/29",
            "10.42.97.80/28",
            "10.16.8.88/29",
            "10.255.191.0/25",
        ]
    },
}
# NetmikoBaseException
# ├── ConfigInvalidException
# ├── ConnectionException
# └── ReadException
#    └── ReadTimeout
# paramiko.ssh_exception.SSHException
# ├── NetmikoTimeoutException
# └── paramiko.ssh_exception.AuthenticationException
#    └── netmiko.exceptions.NetmikoAuthenticationException


exc = {
    "NetmikoBaseException": {
        "ConfigInvalidException": {},
        "ConnectionException": {},
        "ReadException": {"ReadTimeout": []},
    },
    "paramiko.ssh_exception.SSHException": {
        "NetmikoTimeoutException": {},
        "paramiko.ssh_exception.AuthenticationException": {
            "netmiko.exceptions.NetmikoAuthenticationException": []
        },
    },
    "ValueError": {},
}


tree = Tree("Exception")

for vrf_name, params in exc.items():
    vrf_tree = tree.add(f"{vrf_name}")
    for param, details in params.items():
        param_tree = vrf_tree.add(f"{param}")
        # param_tree = vrf_tree.add(f"[green]{param}", expanded=False)
        if type(details) == str:
            details = [details]
        for det in details:
            param_tree.add(det)
print(tree)
