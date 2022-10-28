import csv
from pprint import pprint

with open("csv_files/rib_table.csv") as f:
    reader_data = csv.reader(f)
    headers = next(reader_data)
    print(f"{headers=}")
    for row in reader_data:
        # print(row)
        print([row[1], row[2], row[3]])
