import csv
from pprint import pprint

filename = "csv_files/sw_data_del.csv"
with open(filename) as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        pprint(row)
