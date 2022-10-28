import csv
from pprint import pprint

with open("csv_files/rib_table.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        net, mask, nhop = row[1], row[2], row[3]
        if nhop == "200.219.145.45":
            print(net,  mask, nhop)
