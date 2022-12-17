import sqlite3
import logging

logging.basicConfig(
    format="{asctime} {name} {levelname} {message}",
    datefmt="%H:%M:%S",
    style="{",
    level=logging.DEBUG,
)

data = [
    ("0000.AAAA.CCCC", "sw1", "Cisco 3750", "London, Green Str"),
    ("0000.BBBB.CCCC", "sw2", "Cisco 3780", "London, Green Str"),
    ("0000.AAAA.DDDD", "sw3", "Cisco 2960", "London, Green Str"),
    ("0011.AAAA.CCCC", "sw4", "Cisco 3750", "London, Green Str"),
    ("0050.AAAA.CCCC", "sw5", "Cisco 3950", "London, Globe Str"),
    ("0060.BBBB.CCCC", "sw6", "Cisco 3880", "London, Globe Str"),
    ("0070.AAAA.DDDD", "sw7", "Cisco 2960", "London, Globe Str"),
    ("0081.AAAA.CCCC", "sw8", "Cisco 3750", "London, Globe Str"),
]

query_create = """
create table switch (
    mac text not NULL primary key,
    hostname text,
    model text,
    location text
)
"""
query_insert = "INSERT into switch values (?, ?, ?, ?)"

con = sqlite3.connect("switch_inv_14.db")
con.set_trace_callback(logging.debug)

con.execute(query_create)

for row in data:
    con.execute(query_insert, row)

con.commit()
con.close()
