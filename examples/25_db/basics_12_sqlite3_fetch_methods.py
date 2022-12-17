import sqlite3


query_select = "SELECT * from switch"

# fetchone
con = sqlite3.connect("switch_inv_12.db")
cursor = con.cursor()

cursor.execute(query_select)
while True:
    record = cursor.fetchone()
    print(record)
    if record is None:
        break


# fetchmany
cursor.execute(query_select)
cursor.fetchmany(10)


# fetchall
cursor.execute(query_select)
cursor.fetchall()

con.close()
