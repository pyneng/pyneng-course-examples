# -*- coding: utf-8 -*-
import csv
from glob import glob
import sqlite3
from pprint import pprint
import re


# create DB, tables
db_name = "net_interfaces_ex01.db"
schema = "ex01_db_schema.sql"

con = sqlite3.connect(db_name)

with open(schema) as s:
    con.executescript(s.read())


# add devices
devices_csv = "ex01_routers.csv"
insert_csv = "INSERT into devices values (:ip, :hostname, :location)"

with open(devices_csv) as d:
    reader = csv.DictReader(d)
    with con:
        for row in reader:
            con.execute(insert_csv, row)

# parse interfaces
intf_files = sorted(glob("show_output/sh_ip_int_br_*.txt"))
insert_intf = "INSERT into interfaces values (?, ?, ?, ?)"

regex = re.compile(
    r"(\S+) +(\S+) +\w+ +\w+ +(?:administratively down|up|down) +(up|down)"
)

for intf_f in intf_files:
    device = intf_f.split("_")[-1].split(".")[0]
    with open(intf_f) as f:
        for line in f:
            match_intf = regex.search(line)
            if match_intf:
                intf, ip, status = match_intf.groups()
                if ip == "unassigned":
                    ip = None
                with con:
                    con.execute(insert_intf, [device, intf, ip, status])

con.close()
