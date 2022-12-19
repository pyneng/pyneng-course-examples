# -*- coding: utf-8 -*-
import sqlite3
from pprint import pprint
from tabulate import tabulate


#
db_name = "net_interfaces_ex01.db"
con = sqlite3.connect(db_name)

rows = list(con.execute("select * from devices"))
intf_rows = list(con.execute("select * from interfaces"))

con.close()


print(tabulate(rows))
print(tabulate(intf_rows))
