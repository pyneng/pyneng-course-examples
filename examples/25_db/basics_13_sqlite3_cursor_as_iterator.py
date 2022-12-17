import sqlite3


query_select = "SELECT * from switch"
con = sqlite3.connect("switch_inv_13.db")
cursor = con.cursor()

# cursor as iterator
cursor.execute(query_select)
for row in cursor:
    print(row)


for row in cursor.execute(query_select):
    print(row)

con.close()


# output without cursor
con = sqlite3.connect("switch_inv_13.db")

for row in con.execute(query_select):
    print(row)
con.close()
