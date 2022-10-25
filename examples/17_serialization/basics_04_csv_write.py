import csv


data = [['hostname', 'vendor', 'model', 'location'],
        ['sw1', 'Cisco', '3750', 'London, Best str'],
        ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
        ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
        ['sw4', 'Cisco', '3650', 'London Best str']]


with open("csv_files/result_04.csv", "w") as f:
    wr = csv.writer(f)
    for dlist in data:
        wr.writerow(dlist)

