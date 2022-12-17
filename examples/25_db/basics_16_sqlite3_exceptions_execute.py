import sqlite3
import logging

logging.basicConfig(
    format="{asctime} {name} {levelname} {message}",
    datefmt="%H:%M:%S",
    style="{",
    level=logging.DEBUG,
)


query_create = """
create table if not exists switch (
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
    ("0030.AAAA.CCCC", "sw11", "Cisco 3750", "London, Green Str"),
    ("0020.BBBB.CCCC", "sw12", "Cisco 3780", "London, Green Str"),
    ("0070.AAAA.DDDD", "sw23", "Cisco 2960", "London, Green Str"),
]

con = sqlite3.connect("switch_inv_16.db")
con.set_trace_callback(logging.debug)

con.execute(query_create)

for row in data:
    with con:
        try:
            con.execute(query_insert, row)
        except sqlite3.IntegrityError as error:
            print(error, row)

# try:
#     for row in data:
#         with con:
#             con.execute(query_insert, row)
# except sqlite3.IntegrityError as error:
#     print(error)

con.close()
