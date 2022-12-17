import sqlite3
import logging

query_create = """
create table switch (
    mac text not NULL primary key,
    hostname text,
    model text,
    location text
)
"""
query_insert = "INSERT into switch values (?, ?, ?, ?)"
query_select = "SELECT * from switch"

data = [
    ("0010.AAAA.CCCC", "sw1", "Cisco 3750", "London, Green Str"),
    ("0020.BBBB.CCCC", "sw2", "Cisco 3780", "London, Green Str"),
    ("0030.AAAA.DDDD", "sw3", "Cisco 2960", "London, Green Str"),
    ("0041.AAAA.CCCC", "sw4", "Cisco 3750", "London, Green Str"),
    ("0050.AAAA.CCCC", "sw5", "Cisco 3950", "London, Globe Str"),
    ("0060.BBBB.CCCC", "sw6", "Cisco 3880", "London, Globe Str"),
    ("0070.AAAA.DDDD", "sw7", "Cisco 2960", "London, Globe Str"),
    ("0081.AAAA.CCCC", "sw8", "Cisco 3750", "London, Globe Str"),
]


logging.basicConfig(
    format="{asctime} {name} {levelname} {message}",
    datefmt="%H:%M:%S",
    style="{",
    level=logging.DEBUG,
)

con = sqlite3.connect("switch_inv_12.db")
con.set_trace_callback(logging.debug)
cursor = con.cursor()

cursor.execute(query_create)
cursor.executemany(query_insert, data)

con.commit()
con.close()
