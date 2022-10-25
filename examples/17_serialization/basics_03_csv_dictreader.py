import csv
from pprint import pprint

filename = "csv_files/sw_data.csv"
with open(filename) as f:
    reader = csv.DictReader(f)
    for row in reader:
        pprint(row, width=120, sort_dicts=False)
