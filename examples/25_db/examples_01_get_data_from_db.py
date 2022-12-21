# -*- coding: utf-8 -*-
import sqlite3
from pprint import pprint
import sys
from tabulate import tabulate


select_dict = {
    "device": "SELECT * from interfaces where device = ?",
    "interface": "SELECT * from interfaces where interface = ?",
    "ip": "SELECT * from interfaces where ip = ?",
    "status": "SELECT * from interfaces where status = ?",
}


db_name = "net_interfaces_ex01.db"

con = sqlite3.connect(db_name)

print(sys.argv)
arg_list = sys.argv[1:]
select_intf_all = "SELECT * from interfaces"

if len(arg_list) == 0:
    intf_list = list(con.execute(select_intf_all))
else:
    param, value = arg_list
    select_intf = select_dict.get(param)
    if select_intf is None:
        intf_list = list(con.execute(select_intf_all))
    else:
        intf_list = list(con.execute(select_intf, [value]))

select_dev = "SELECT * from devices"
dev_list = list(con.execute(select_dev))

select_headers = 'select name from pragma_table_info("{}")'

headers_intf = []
for row in con.execute(select_headers.format("interfaces")):
    headers_intf.extend(row)

print(
    tabulate(intf_list, tablefmt="pipe", headers=headers_intf)
)
print("\n")
headers_dev = []
for row in con.execute(select_headers.format("devices")):
    headers_dev.extend(row)

# print(tabulate(dev_list, tablefmt="pipe", headers="ip hostname location".split()))
