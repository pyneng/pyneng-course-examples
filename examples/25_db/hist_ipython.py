 1/1: import os
 1/2: os.environ
 1/3: os.environ["GITHUB_TOKEN"]
 2/1: import os
 2/2: os.environ["GITHUB_TOKEN"]
 3/1: .exit
 4/1: import sqlite3
 4/2: conn = sqlite3.connect("switch_inv_10.db")
 4/3: conn
 4/4: cursor = conn.cursor()
 4/5: cursor
 4/6: from rich import inspect
 4/7: inspect(cursor, methods=True)
 4/8: inspect(conn, methods=True)
 5/1: import sqlite3
 5/2: from rich import inspect
 5/3: import sqlite3
 5/4: import sqlite3
 5/5: con = sqlite3.connect("switch_inv_10.db")
 5/6: con
 5/7: inspect(con, methods=True)
 5/8: import sqlite3
 5/9: con = sqlite3.connect("switch_inv_10.db")
5/10: con
5/11: inspect(con, methods=True)
 6/1: from rich import inspect
 6/2: import sqlite3
 6/3: con = sqlite3.connect("switch_inv_10.db")
 6/4: con
 6/5: inspect(con, methods=True)
 6/6: con = sqlite3.connect("switch_inv_10.db")
 6/7: cursor = con.cursor()
 6/8: cursor
 6/9: inspect(cursor, methods=True)
 7/1: import sqlite3
 7/2: con = sqlite3.connect("switch_inv_10.db")
 7/3: cursor = con.cursor()
 7/4:
query = """
create table switch (
    mac text not NULL primary key,
    hostname text,
    model text,
    location text
)
"""
 7/5: cursor.execute(query)
 7/6: cursor.execute(query)
 7/7:
data = [('0000.AAAA.CCCC', 'sw1', 'Cisco 3750', 'London, Green Str'),
        ('0000.BBBB.CCCC', 'sw2', 'Cisco 3780', 'London, Green Str'),
        ('0000.AAAA.DDDD', 'sw3', 'Cisco 2960', 'London, Green Str'),
        ('0011.AAAA.CCCC', 'sw4', 'Cisco 3750', 'London, Green Str')]
 8/1: import sqlite3
 8/2: con = sqlite3.connect("switch_inv_10.db")
 8/3: cursor = con.cursor()
 8/4:
query = """
create table switch (
    mac text not NULL primary key,
    hostname text,
    model text,
    location text
)
"""
 8/5: q
 9/1: import sqlite3
 9/2: con = sqlite3.connect("switch_inv_10.db")
 9/3: cursor = con.cursor()
 9/4:
query = """
create table switch (
    mac text not NULL primary key,
    hostname text,
    model text,
    location text
)
"""
 9/5: cursor.execute(query)
 9/6: cursor.execute(query)
 9/7:
data = [('0000.AAAA.CCCC', 'sw1', 'Cisco 3750', 'London, Green Str'),
        ('0000.BBBB.CCCC', 'sw2', 'Cisco 3780', 'London, Green Str'),
        ('0000.AAAA.DDDD', 'sw3', 'Cisco 2960', 'London, Green Str'),
        ('0011.AAAA.CCCC', 'sw4', 'Cisco 3750', 'London, Green Str')]
 9/8: q_insert = "INSERT intro switch values (?, ?, ?, ?)"
 9/9:
for item in data:
    cursor.execute(q_insert, item)
10/1: import sqlite3
10/2: con = sqlite3.connect("switch_inv_10.db")
10/3: cursor = con.cursor()
10/4:
query = """
create table switch (
    mac text not NULL primary key,
    hostname text,
    model text,
    location text
)
"""
10/5: cursor.execute(query)
11/1: import sqlite3
11/2: import sqlite3
12/1: import sqlite3
12/2: con = sqlite3.connect("switch_inv_10.db")
12/3: cursor = con.cursor()
12/4:
query = """
create table switch (
    mac text not NULL primary key,
    hostname text,
    model text,
    location text
)
"""
12/5: cursor.execute(query)
12/6:
data = [('0000.AAAA.CCCC', 'sw1', 'Cisco 3750', 'London, Green Str'),
        ('0000.BBBB.CCCC', 'sw2', 'Cisco 3780', 'London, Green Str'),
        ('0000.AAAA.DDDD', 'sw3', 'Cisco 2960', 'London, Green Str'),
        ('0011.AAAA.CCCC', 'sw4', 'Cisco 3750', 'London, Green Str')]
12/7: q_insert = "INSERT into switch values (?, ?, ?, ?)")
12/8:
data = [('0000.AAAA.CCCC', 'sw1', 'Cisco 3750', 'London, Green Str'),
        ('0000.BBBB.CCCC', 'sw2', 'Cisco 3780', 'London, Green Str'),
        ('0000.AAAA.DDDD', 'sw3', 'Cisco 2960', 'London, Green Str'),
        ('0011.AAAA.CCCC', 'sw4', 'Cisco 3750', 'London, Green Str')]
12/9: ins_q = "INSERT into switch values (?, ?, ?, ?)")
12/10:
data = [('0000.AAAA.CCCC', 'sw1', 'Cisco 3750', 'London, Green Str'),
        ('0000.BBBB.CCCC', 'sw2', 'Cisco 3780', 'London, Green Str'),
        ('0000.AAAA.DDDD', 'sw3', 'Cisco 2960', 'London, Green Str'),
        ('0011.AAAA.CCCC', 'sw4', 'Cisco 3750', 'London, Green Str')]
12/11: qi = "INSERT into switch values (?, ?, ?, ?)"
12/12:
for row in data:
    cursor.execute(qi, row)
12/13: qs = "SELECT * from switch"
12/14: cursor.execute(qs)
12/15: cursor.fetchall()
12/16: con.close()
12/17: con = sqlite3.connect("switch_inv_10.db")
12/18: cursor = con.cursor()
12/19: cursor.execute(qs)
12/20: cursor.fetchall()
12/21: con.commit()
12/22:
data = [('0000.AAAA.CCCC', 'sw1', 'Cisco 3750', 'London, Green Str'),
        ('0000.BBBB.CCCC', 'sw2', 'Cisco 3780', 'London, Green Str'),
        ('0000.AAAA.DDDD', 'sw3', 'Cisco 2960', 'London, Green Str'),
        ('0011.AAAA.CCCC', 'sw4', 'Cisco 3750', 'London, Green Str')]
12/23: qi
12/24:
for row in data:
    cursor.execute(qi, row)
12/25: con.commit()
13/1: import sqlite3
13/2: con = sqlite3.connect("switch_inv_11.db")
16/1: import sqlite3
16/2: con = sqlite3.connect("switch_inv_11.db")
17/1: import sqlite3
17/2: con = sqlite3.connect("switch_inv_11.db")
17/3: cursor = con.cursor()
17/4: cursor.execute(query_create)
17/5: cursor.executescript(query_create)
17/6:
for row in data:
    cursor.execute(query_insert, row)
17/7: con.commit()
17/8: cursor.executemany(query_insert_adm, admins)
17/9: con.commit()
17/10: adm3 = {"email": "tom@gmail.com", "name": "Tom Green", "permissions": 55}
17/11: cursor.execute(query_insert_adm, adm3)
17/12: con.commit()
18/1: import sqlite3
18/2: con = sqlite3.connect("switch_inv_12.db")
18/3: cursor = con.cursor()
18/4: cursor.execute("select * from switch")
18/5: cursor.fetchone()
18/6: cursor.fetchone()
18/7: cursor.fetchone()
18/8: cursor.fetchone()
18/9: cursor.fetchone()
18/10: cursor.fetchone()
18/11: cursor.fetchone()
18/12: cursor.fetchone()
18/13: cursor.fetchone()
18/14: cursor.fetchone()
19/1: import sqlite3
19/2: con = sqlite3.connect("switch_inv_12.db")
19/3: cursor = con.cursor()
19/4: cursor.execute("select * from switch")
19/5: cursor.fetchone()
19/6: cursor.fetchone()
19/7: cursor.fetchone()
19/8: cursor.fetchone()
19/9: cursor.fetchone()
19/10: cursor.fetchone()
19/11: cursor.fetchone()
19/12: cursor.fetchone()
19/13: cursor.fetchone()
19/14: cursor.execute("select * from switch")
19/15: cursor.fetchmany?
19/16: cursor.fetchmany()
19/17: cursor.fetchmany(10)
19/18: cursor.execute("select * from switch")
19/19: cursor.fetchmany(10000)
19/20: cursor.execute("select * from switch")
19/21: cursor.fetchall()
19/22: cursor.execute("select * from switch")
19/23:
for row in cursor:
    print(row)
19/24: id(cursor)
19/25: id(cursor.execute("select * from switch"))
19/26: cursor.execute("select * from switch")
19/27: cursor.fetchall()
19/28: cursor.execute("select * from switch")
19/29:
for row in cursor:
    print(row)
19/30:
for row in cursor.execute("select * from switch"):
    print(row)
19/31: id(cursor)
19/32: id(cursor.execute("select * from switch"))
19/33: con = sqlite3.connect("switch_inv_12.db")
19/34:
for row in con.execute("select * from switch"):
    print(row)
19/35: con.execute("select * from switch")
19/36: cursor = con.cursor()
19/37: [a for a in dir(cursor) if not a.startswith("__")]
19/38: [a for a in dir(cursor) if not a.startswith("__")]
19/39: [a for a in dir(con) if not a.startswith("__")]
19/40: con = sqlite3.connect("switch_inv_12.db")
19/41: cursor = con.execute("select * from switch")
19/42:
for row in cursor:
    print(row)
19/43: cursor_dir = [a for a in dir(cursor) if not a.startswith("__")]
19/44: con_dir = {a for a in dir(con) if not a.startswith("__")}
19/45: cursor_dir = {a for a in dir(cursor) if not a.startswith("__")}
19/46: cursor_dir - con_dir
19/47: con_dir - cursor_dir
   1: %history -g -f hist_ipython.py
