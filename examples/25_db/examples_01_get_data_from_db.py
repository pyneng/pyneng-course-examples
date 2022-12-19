# -*- coding: utf-8 -*-
import sqlite3
from pprint import pprint
from tabulate import tabulate


def get_table_headers(con, table):
    headers = []
    q = f"SELECT name FROM pragma_table_info('{table}')"
    for row in con.execute(q):
        headers.extend(row)
    return headers


#
db_name = "net_interfaces_ex01.db"
con = sqlite3.connect(db_name)

headers_dev = get_table_headers(con, "devices")
dev_rows = list(con.execute("select * from devices"))
headers_intf = get_table_headers(con, "interfaces")
intf_rows = list(con.execute("select * from interfaces"))

con.close()


print(tabulate(dev_rows, headers=headers_dev))
print(tabulate(intf_rows, headers=headers_intf))
# print(tabulate(dev_rows))
# print(tabulate(intf_rows))
