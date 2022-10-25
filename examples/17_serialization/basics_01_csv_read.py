import csv
from pprint import pprint

filename = "csv_files/sw_data.csv"
with open(filename) as f:
    reader = csv.reader(f)
    headers = next(reader)
    print(f"{headers=}")
    for row in reader:
        pprint(row)
