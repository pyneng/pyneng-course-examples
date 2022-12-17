import sqlite3
import logging

logging.basicConfig(
    format="{asctime} {name} {levelname} {message}",
    datefmt="%H:%M:%S",
    style="{",
    level=logging.DEBUG,
)


query_create = """
create table switch (
    mac text not NULL primary key,
    hostname text,
    model text,
    location text
)
"""
query_insert = "INSERT into switch values (?, ?, ?, ?)"

data = [
    ("0000.AAAA.CCCC", "sw1", "Cisco 3750", "London, Green Str"),
    ("0000.BBBB.CCCC", "sw2", "Cisco 3780", "London, Green Str"),
    ("0000.AAAA.DDDD", "sw3", "Cisco 2960", "London, Green Str"),
    ("0011.AAAA.CCCC", "sw4", "Cisco 3750", "London, Green Str"),
    ("0011.AAAA.CCCC", "sw5", "Cisco 3750", "London, Globe Str"),
]

con = sqlite3.connect("switch_inv_15.db")
con.set_trace_callback(logging.debug)

con.execute(query_create)

# with con:
#     try:
#         con.executemany(query_insert, data)
#     except sqlite3.IntegrityError as error:
#         print(error)

try:
    with con:
        con.executemany(query_insert, data)
except sqlite3.IntegrityError as error:
    print(error)

con.close()
