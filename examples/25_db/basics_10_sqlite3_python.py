import sqlite3
import logging


logging.basicConfig(
    format="{asctime} {name} {levelname} {message}",
    datefmt="%H:%M:%S",
    style="{",
    level=logging.DEBUG,
)


conn = sqlite3.connect("rib_database.db")
conn.set_trace_callback(logging.debug)

for row in conn.execute('select * from rib limit 10'):
    print(row)

conn.close()
