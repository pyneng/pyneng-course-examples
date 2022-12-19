import sqlite3
import logging
from rich.logging import RichHandler


logging.basicConfig(
    format="{message}",
    datefmt="%H:%M:%S",
    style="{",
    level=logging.DEBUG,
    handlers=[RichHandler()]
)

data = [('0000.AAAA.CCCC', 'sw1', 'Cisco 3750', 'London, Green Str'),
        ('0000.BBBB.CCCC', 'sw2', 'Cisco 3780', 'London, Green Str'),
        ('0000.AAAA.DDDD', 'sw3', 'Cisco 2960', 'London, Green Str'),
        ('0011.AAAA.CCCC', 'sw4', 'Cisco 3750', 'London, Green Str')]


con = sqlite3.connect('sw_inventory2.db')
con.set_trace_callback(logging.debug)

con.execute('''create table if not exists switch
            (mac text not NULL primary key, hostname text, model text, location text)'''
            )

query = 'INSERT into switch values (?, ?, ?, ?)'

with con:
    con.executemany(query, data)

for row in con.execute('select * from switch'):
    print(row)

con.close()
