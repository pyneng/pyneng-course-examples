import csv
from pprint import pprint


with open("csv_files/rib_table.csv") as f, open("csv_files/result_ex03.csv", "w") as dst:
    reader = csv.DictReader(f)
    writer = csv.writer(dst)
    headers = ["network", "netmask", "nexthop"]
    writer.writerow(headers)
    for row in reader:
        values = [row[key] for key in headers]
        writer.writerow(values)
