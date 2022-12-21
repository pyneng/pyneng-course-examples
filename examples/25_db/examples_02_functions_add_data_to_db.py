# -*- coding: utf-8 -*-
import csv
from glob import glob
import sqlite3
from pprint import pprint
import re


def create_db_tables(database_name, schema_str):
    con = sqlite3.connect(database_name)
    con.executescript(schema_str)
    con.close()


def fill_devices_table(database_name, devices_csv_filename):
    con = sqlite3.connect(database_name)
    insert_csv = "INSERT into devices values (:ip, :hostname, :location)"

    with open(devices_csv_filename) as d:
        reader = csv.DictReader(d)
        with con:
            for row in reader:
                con.execute(insert_csv, row)
    con.close()


def parse_sh_ip_int_br(output):
    regex = re.compile(
        r"(\S+) +(\S+) +\w+ +\w+ +(?:administratively down|up|down) +(up|down)"
    )
    result_list = []
    for line in output.split("\n"):
        match_intf = regex.search(line)
        if match_intf:
            intf, ip, status = match_intf.groups()
            if ip == "unassigned":
                ip = None
            result_list.append([intf, ip, status])
    return result_list


def fill_interfaces_table(database_name, intf_file_list):
    con = sqlite3.connect(database_name)
    insert_intf = "INSERT into interfaces values (?, ?, ?, ?)"

    for intf_f in intf_file_list:
        device = intf_f.split("_")[-1].split(".")[0]
        with open(intf_f) as f:
            out = f.read()
        parsed_out = parse_sh_ip_int_br(out)
        for intf, ip, status in parsed_out:
            with con:
                con.execute(insert_intf, [device, intf, ip, status])

    con.close()


if __name__ == "__main__":
    db_name = "net_interfaces_ex02.db"
    schema = "ex01_db_schema.sql"
    devices_csv = "ex01_routers.csv"
    intf_files = sorted(glob("show_output/sh_ip_int_br_*.txt"))
    with open(schema) as s:
        s_out = s.read()
    create_db_tables(db_name, s_out)
    fill_devices_table(db_name, devices_csv)
    fill_interfaces_table(db_name, intf_files)
