# -*- coding: utf-8 -*-
import sqlite3
from pprint import pprint
import sys
from tabulate import tabulate


def get_table_headers(connection, table_name):
    select_headers = f'select name from pragma_table_info("{table_name}")'
    headers = []
    for row in connection.execute(select_headers):
        headers.extend(row)
    return headers


def get_all_from_interfaces(database_name):
    con = sqlite3.connect(database_name)
    select_intf_all = "SELECT * from interfaces"
    intf_list = list(con.execute(select_intf_all))
    headers_intf = get_table_headers(con, "interfaces")
    print(
        tabulate(intf_list, tablefmt="pipe", headers=headers_intf)
    )
    con.close()


def get_param_from_interfaces(database_name, param_name, param_value):
    con = sqlite3.connect(database_name)
    select_dict = {
        "device": "SELECT * from interfaces where device = ?",
        "interface": "SELECT * from interfaces where interface = ?",
        "ip": "SELECT * from interfaces where ip = ?",
        "status": "SELECT * from interfaces where status = ?",
    }
    select_intf = select_dict.get(param_name)
    headers_intf = get_table_headers(con, "interfaces")
    if select_intf is None:
        get_all_from_interfaces(database_name)
    else:
        intf_list = list(con.execute(select_intf, [param_value]))
        print(
            tabulate(intf_list, tablefmt="pipe", headers=headers_intf)
        )
    con.close()


def get_all_from_devices(database_name):
    con = sqlite3.connect(database_name)
    headers_dev = get_table_headers(con, "devices")
    select_dev = "SELECT * from devices"
    dev_list = list(con.execute(select_dev))
    print(
        tabulate(dev_list, tablefmt="pipe", headers=headers_dev)
    )
    con.close()


def print_tables(db_name, arg_list):
    get_all_from_devices(db_name)
    print("\n")
    if len(arg_list) == 0:
        get_all_from_interfaces(db_name)
    elif len(arg_list) == 2:
        param, value = arg_list
        get_param_from_interfaces(db_name, param, value)
    else:
        print("Pass 0 or 2 args")


if __name__ == "__main__":
    db_name = "net_interfaces_ex02.db"
    arg_list = sys.argv[1:]
    print_tables(db_name, arg_list)

