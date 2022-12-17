import sqlite3
import logging

query_create = """
create table switch (
    mac text not NULL primary key,
    hostname text,
    model text,
    location text
);
create table admins (
    email text not NULL primary key,
    name text,
    permissions integer CHECK (permissions in (0, 10, 20)) 
);
"""
query_insert = "INSERT into switch values (?, ?, ?, ?)"
query_insert_adm = "INSERT into admins values (:email, :name, :permissions)"
query_select = "SELECT * from switch"

data = [
    ("0000.AAAA.CCCC", "sw1", "Cisco 3750", "London, Green Str"),
    ("0000.BBBB.CCCC", "sw2", "Cisco 3780", "London, Green Str"),
    ("0000.AAAA.DDDD", "sw3", "Cisco 2960", "London, Green Str"),
    ("0011.AAAA.CCCC", "sw4", "Cisco 3750", "London, Green Str"),
]

admins = [
    {"email": "john@gmail.com", "name": "John Brown", "permissions": 10},
    {"email": "jessica@gmail.com", "name": "Jessica Newman", "permissions": 0},
    # {"email": "tom@gmail.com", "name": "Tom Green", "permissions": 55},
]

logging.basicConfig(
    format="{asctime} {name} {levelname} {message}",
    datefmt="%H:%M:%S",
    style="{",
    level=logging.DEBUG,
)


con = sqlite3.connect("switch_inv_11.db")
con.set_trace_callback(logging.debug)
cursor = con.cursor()

cursor.executescript(query_create)

for row in data:
    cursor.execute(query_insert, row)

# for row_dict in admins:
#     cursor.execute(query_insert_adm, row_dict)
cursor.executemany(query_insert_adm, admins)

con.commit()
con.close()
