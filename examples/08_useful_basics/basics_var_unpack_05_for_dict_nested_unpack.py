
inv_data_dict = {
    "10.1.1.1": ["London_PE1", "Cisco"],
    "10.2.2.2": ["London_PE2", "Cisco"],
    "10.3.3.3": ["London_PE3", "Cisco"],
}


for ip, (hostname, vendor) in inv_data_dict.items():
    print(ip, hostname, vendor)
