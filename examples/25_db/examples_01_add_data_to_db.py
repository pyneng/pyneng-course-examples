# -*- coding: utf-8 -*-
import csv
from glob import glob
import sqlite3
from pprint import pprint

from examples_01_get_output import parse_sh_ip_int_br, parse_show_output


# create DB, tables
db_name = "net_interfaces_ex01.db"
schema = "ex01_db_schema.sql"

con = sqlite3.connect(db_name)

with open(schema) as s:
    con.executescript(s.read())


# add devices
devices_csv = "ex01_routers.csv"
insert_query = "INSERT into devices values (:ip, :hostname, :location)"

with open(devices_csv) as f:
    reader = csv.DictReader(f)
    with con:
        for row in reader:
            con.execute(insert_query, row)

# parse interfaces
intf_files = glob("show_output/sh_ip_int_br_*.txt")

intf_list = []
for intf_f in intf_files:
    with open(intf_f) as f:
        out = f.read()
    device = intf_f.split("_")[-1].split(".")[-2]
    parsed_out = parse_sh_ip_int_br(out)
    for intf, ip, _, status in parsed_out:
        if ip == "unassigned":
            ip = None
        intf_tuple = (device, intf, ip, status)
        intf_list.append(intf_tuple)

# add interfaces
insert_query = "INSERT into interfaces values (?, ?, ?, ?)"
with con:
    con.executemany(insert_query, intf_list)


for row in con.execute("select * from devices"):
    print(row)
for row in con.execute("select * from interfaces"):
    print(row)

con.close()
