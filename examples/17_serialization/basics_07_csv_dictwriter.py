import csv


data = [
    {"hostname": "sw1", "location": "London", "model": "3750", "vendor": "Cisco"},
    {"hostname": "sw2", "location": "Liverpool", "model": "3850", "vendor": "Cisco"},
    {"hostname": "sw3", "location": "Liverpool", "model": "3650", "vendor": "Cisco"},
    {"hostname": "sw4", "location": "London", "model": "3650", "vendor": "Cisco"},
]
headers = "hostname location model vendor".split()

with open("csv_files/result_07.csv", "w") as f:
    wr = csv.DictWriter(f, fieldnames=headers, delimiter=";")
    wr.writeheader()
    # wr.writerows(data)
    for ddict in data:
        wr.writerow(ddict)
