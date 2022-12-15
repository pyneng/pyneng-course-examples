
# 2022-12-15 06:52:28.451364
select * from switch
+----------------+----------+------------+-------------------+------------+-----------+
| mac            | hostname | model      | location          | mngmt_ip   | mngmt_vid |
+----------------+----------+------------+-------------------+------------+-----------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str | <null>     | 255       |
| 0010.A1AA.21CC | sw101    | Cisco 3750 | London, Green Str | 10.1.1.101 | 255       |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str | <null>     | 255       |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str | <null>     | 255       |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str | <null>     | 255       |
| 0110.A10A.C1CC | sw10     | 3750       | London, Green Str | <null>     | 255       |
+----------------+----------+------------+-------------------+------------+-----------+
9 rows in set
Time: 0.050s

# 2022-12-15 07:07:40.056271
.exit
Goodbye!

# 2022-12-15 07:07:46.460008
select * from switch
+----------------+----------+------------+-------------------+------------+-----------+
| mac            | hostname | model      | location          | mngmt_ip   | mngmt_vid |
+----------------+----------+------------+-------------------+------------+-----------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str | <null>     | 255       |
| 0010.A1AA.21CC | sw101    | Cisco 3750 | London, Green Str | 10.1.1.101 | 255       |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str | <null>     | 255       |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str | <null>     | 255       |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str | <null>     | 255       |
| 0110.A10A.C1CC | sw10     | 3750       | London, Green Str | <null>     | 255       |
+----------------+----------+------------+-------------------+------------+-----------+
9 rows in set
Time: 0.041s

# 2022-12-15 07:08:04.040091
.schema
+-----------------------------------------------+
| sql                                           |
+-----------------------------------------------+
| CREATE TABLE switch (                         |
|     mac text not NULL primary key,            |
|     hostname text,                            |
|     model text,                               |
|     location text                             |
| , mngmt_ip text, mngmt_vid integer default 1) |
| <null>                                        |
+-----------------------------------------------+
Time: 0.033s

# 2022-12-15 07:08:15.219925
select * from switch
+----------------+----------+------------+-------------------+------------+-----------+
| mac            | hostname | model      | location          | mngmt_ip   | mngmt_vid |
+----------------+----------+------------+-------------------+------------+-----------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str | <null>     | 255       |
| 0010.A1AA.21CC | sw101    | Cisco 3750 | London, Green Str | 10.1.1.101 | 255       |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str | <null>     | 255       |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str | <null>     | 255       |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str | <null>     | 255       |
| 0110.A10A.C1CC | sw10     | 3750       | London, Green Str | <null>     | 255       |
+----------------+----------+------------+-------------------+------------+-----------+
9 rows in set
Time: 0.022s

# 2022-12-15 07:08:18.556950
.schema switch
+-----------------------------------------------+
| sql                                           |
+-----------------------------------------------+
| CREATE TABLE switch (                         |
|     mac text not NULL primary key,            |
|     hostname text,                            |
|     model text,                               |
|     location text                             |
| , mngmt_ip text, mngmt_vid integer default 1) |
+-----------------------------------------------+
Time: 0.019s

# 2022-12-15 07:08:44.886666
select * from switch
+----------------+----------+------------+-------------------+------------+-----------+
| mac            | hostname | model      | location          | mngmt_ip   | mngmt_vid |
+----------------+----------+------------+-------------------+------------+-----------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str | <null>     | 255       |
| 0010.A1AA.21CC | sw101    | Cisco 3750 | London, Green Str | 10.1.1.101 | 255       |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str | <null>     | 255       |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str | <null>     | 255       |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str | <null>     | 255       |
| 0110.A10A.C1CC | sw10     | 3750       | London, Green Str | <null>     | 255       |
+----------------+----------+------------+-------------------+------------+-----------+
9 rows in set
Time: 0.023s

# 2022-12-15 07:09:35.525719
insert into switch values ('0010.A1AA.C1CC', 'sw1', "Cisco 3850", 'London, Green Str')
table switch has 6 columns but 4 values were supplied

# 2022-12-15 07:09:52.673984
select * from switch
+----------------+----------+------------+-------------------+------------+-----------+
| mac            | hostname | model      | location          | mngmt_ip   | mngmt_vid |
+----------------+----------+------------+-------------------+------------+-----------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str | <null>     | 255       |
| 0010.A1AA.21CC | sw101    | Cisco 3750 | London, Green Str | 10.1.1.101 | 255       |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str | <null>     | 255       |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str | <null>     | 255       |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str | <null>     | 255       |
| 0110.A10A.C1CC | sw10     | 3750       | London, Green Str | <null>     | 255       |
+----------------+----------+------------+-------------------+------------+-----------+
9 rows in set
Time: 0.019s

# 2022-12-15 07:10:49.849280
insert into switch values ('0010.A1AA.C1CC', 'sw1', "Cisco 3850", 'London, Green Str')
table switch has 6 columns but 4 values were supplied

# 2022-12-15 07:11:23.357425
insert into switch values ('0010.A1AA.C1CC', 'sw1', "Cisco 3850", 'London, Green Str', "10.1.1.1", 254)
UNIQUE constraint failed: switch.mac

# 2022-12-15 07:11:45.223132
.schema switch
+-----------------------------------------------+
| sql                                           |
+-----------------------------------------------+
| CREATE TABLE switch (                         |
|     mac text not NULL primary key,            |
|     hostname text,                            |
|     model text,                               |
|     location text                             |
| , mngmt_ip text, mngmt_vid integer default 1) |
+-----------------------------------------------+
Time: 0.021s

# 2022-12-15 07:12:11.009335
select * from switch
+----------------+----------+------------+-------------------+------------+-----------+
| mac            | hostname | model      | location          | mngmt_ip   | mngmt_vid |
+----------------+----------+------------+-------------------+------------+-----------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str | <null>     | 255       |
| 0010.A1AA.21CC | sw101    | Cisco 3750 | London, Green Str | 10.1.1.101 | 255       |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str | <null>     | 255       |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str | <null>     | 255       |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str | <null>     | 255       |
| 0110.A10A.C1CC | sw10     | 3750       | London, Green Str | <null>     | 255       |
+----------------+----------+------------+-------------------+------------+-----------+
9 rows in set
Time: 0.019s

# 2022-12-15 07:12:13.311712
insert into switch values ('0010.A1AA.C1CC', 'sw1', "Cisco 3850", 'London, Green Str', "10.1.1.1", 254)
UNIQUE constraint failed: switch.mac

# 2022-12-15 07:12:20.652958
insert or replace into switch values ('0010.A1AA.C1CC', 'sw1', "Cisco 3850", 'London, Green Str', "10.1.1.1", 254)
Query OK, 1 row affected
Time: 0.004s

# 2022-12-15 07:12:24.103556
select * from switch
+----------------+----------+------------+-------------------+------------+-----------+
| mac            | hostname | model      | location          | mngmt_ip   | mngmt_vid |
+----------------+----------+------------+-------------------+------------+-----------+
| 0010.A1AA.21CC | sw101    | Cisco 3750 | London, Green Str | 10.1.1.101 | 255       |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str | <null>     | 255       |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str | <null>     | 255       |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str | <null>     | 255       |
| 0110.A10A.C1CC | sw10     | 3750       | London, Green Str | <null>     | 255       |
| 0010.A1AA.C1CC | sw1      | Cisco 3850 | London, Green Str | 10.1.1.1   | 254       |
+----------------+----------+------------+-------------------+------------+-----------+
9 rows in set
Time: 0.022s

# 2022-12-15 07:14:44.202847
.exit
Goodbye!
