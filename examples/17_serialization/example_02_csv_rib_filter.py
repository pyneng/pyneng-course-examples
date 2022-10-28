import csv
from pprint import pprint


with open("csv_files/rib_table.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        pprint(row)
        print(row["network"], row["netmask"], row["nexthop"])
