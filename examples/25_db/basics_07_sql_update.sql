
# 2022-12-15 06:26:31.055114
select * from switch
+----------------+----------+------------+-------------------+
| mac            | hostname | model      | location          |
+----------------+----------+------------+-------------------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str |
| 0010.A1AA.21CC | <null>   | Cisco 3750 | London, Green Str |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str |
| 0110.A10A.C1CC | sw10     | 3750       | London, Green Str |
+----------------+----------+------------+-------------------+
9 rows in set
Time: 0.046s

# 2022-12-15 06:27:44.999625
.exit
Goodbye!

# 2022-12-15 06:29:21.192299
select * from switch
+----------------+----------+------------+-------------------+
| mac            | hostname | model      | location          |
+----------------+----------+------------+-------------------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str |
| 0010.A1AA.21CC | <null>   | Cisco 3750 | London, Green Str |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str |
| 0110.A10A.C1CC | sw10     | 3750       | London, Green Str |
+----------------+----------+------------+-------------------+
9 rows in set
Time: 0.036s
Your call!

# 2022-12-15 06:31:41.178752
alter table switch add column mngmt_ip text
Query OK, 0 rows affected
Time: 0.003s

# 2022-12-15 06:31:44.297192
select * from switch
+----------------+----------+------------+-------------------+----------+
| mac            | hostname | model      | location          | mngmt_ip |
+----------------+----------+------------+-------------------+----------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str | <null>   |
| 0010.A1AA.21CC | <null>   | Cisco 3750 | London, Green Str | <null>   |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str | <null>   |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str | <null>   |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str | <null>   |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str | <null>   |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str | <null>   |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str | <null>   |
| 0110.A10A.C1CC | sw10     | 3750       | London, Green Str | <null>   |
+----------------+----------+------------+-------------------+----------+
9 rows in set
Time: 0.024s

# 2022-12-15 06:31:49.592180
.schema
+------------------------------------+
| sql                                |
+------------------------------------+
| CREATE TABLE switch (              |
|     mac text not NULL primary key, |
|     hostname text,                 |
|     model text,                    |
|     location text                  |
| , mngmt_ip text)                   |
| <null>                             |
+------------------------------------+
Time: 0.019s

# 2022-12-15 06:32:11.744891
allter
near "allter": syntax error
Your call!

# 2022-12-15 06:32:45.826854
alter table switch add column mngmt_vid integer default 1
Query OK, 0 rows affected
Time: 0.032s

# 2022-12-15 06:32:49.538908
select * from switch
+----------------+----------+------------+-------------------+----------+-----------+
| mac            | hostname | model      | location          | mngmt_ip | mngmt_vid |
+----------------+----------+------------+-------------------+----------+-----------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str | <null>   | 1         |
| 0010.A1AA.21CC | <null>   | Cisco 3750 | London, Green Str | <null>   | 1         |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str | <null>   | 1         |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str | <null>   | 1         |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str | <null>   | 1         |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str | <null>   | 1         |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str | <null>   | 1         |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str | <null>   | 1         |
| 0110.A10A.C1CC | sw10     | 3750       | London, Green Str | <null>   | 1         |
+----------------+----------+------------+-------------------+----------+-----------+
9 rows in set
Time: 0.065s

# 2022-12-15 06:34:08.806058
update switch set mngmt_vid = 255
Query OK, 9 rows affected
Time: 0.004s

# 2022-12-15 06:34:18.532303
select * from switch
+----------------+----------+------------+-------------------+----------+-----------+
| mac            | hostname | model      | location          | mngmt_ip | mngmt_vid |
+----------------+----------+------------+-------------------+----------+-----------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str | <null>   | 255       |
| 0010.A1AA.21CC | <null>   | Cisco 3750 | London, Green Str | <null>   | 255       |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str | <null>   | 255       |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str | <null>   | 255       |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str | <null>   | 255       |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str | <null>   | 255       |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str | <null>   | 255       |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str | <null>   | 255       |
| 0110.A10A.C1CC | sw10     | 3750       | London, Green Str | <null>   | 255       |
+----------------+----------+------------+-------------------+----------+-----------+
9 rows in set
Time: 0.024s

# 2022-12-15 06:34:55.215516
select * from switch
+----------------+----------+------------+-------------------+----------+-----------+
| mac            | hostname | model      | location          | mngmt_ip | mngmt_vid |
+----------------+----------+------------+-------------------+----------+-----------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str | <null>   | 255       |
| 0010.A1AA.21CC | <null>   | Cisco 3750 | London, Green Str | <null>   | 255       |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str | <null>   | 255       |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str | <null>   | 255       |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str | <null>   | 255       |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str | <null>   | 255       |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str | <null>   | 255       |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str | <null>   | 255       |
| 0110.A10A.C1CC | sw10     | 3750       | London, Green Str | <null>   | 255       |
+----------------+----------+------------+-------------------+----------+-----------+
9 rows in set
Time: 0.023s

# 2022-12-15 06:39:36.599732
update switch set hostname = "sw100" where mac = "0010.A1AA.21CC"
Query OK, 1 row affected
Time: 0.002s

# 2022-12-15 06:39:38.535406
select * from switch
+----------------+----------+------------+-------------------+----------+-----------+
| mac            | hostname | model      | location          | mngmt_ip | mngmt_vid |
+----------------+----------+------------+-------------------+----------+-----------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str | <null>   | 255       |
| 0010.A1AA.21CC | sw100    | Cisco 3750 | London, Green Str | <null>   | 255       |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str | <null>   | 255       |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str | <null>   | 255       |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str | <null>   | 255       |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str | <null>   | 255       |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str | <null>   | 255       |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str | <null>   | 255       |
| 0110.A10A.C1CC | sw10     | 3750       | London, Green Str | <null>   | 255       |
+----------------+----------+------------+-------------------+----------+-----------+
9 rows in set
Time: 0.027s

# 2022-12-15 06:39:59.938093
select * from switch
+----------------+----------+------------+-------------------+----------+-----------+
| mac            | hostname | model      | location          | mngmt_ip | mngmt_vid |
+----------------+----------+------------+-------------------+----------+-----------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str | <null>   | 255       |
| 0010.A1AA.21CC | sw100    | Cisco 3750 | London, Green Str | <null>   | 255       |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str | <null>   | 255       |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str | <null>   | 255       |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str | <null>   | 255       |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str | <null>   | 255       |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str | <null>   | 255       |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str | <null>   | 255       |
| 0110.A10A.C1CC | sw10     | 3750       | London, Green Str | <null>   | 255       |
+----------------+----------+------------+-------------------+----------+-----------+
9 rows in set
Time: 0.025s

# 2022-12-15 06:40:17.596321
update switch set hostname = "sw101", set mngmt_ip = "10.1.1.101" where mac = "0010.A1AA.21CC"
near "set": syntax error

# 2022-12-15 06:40:23.827961
update switch set hostname = "sw101", mngmt_ip = "10.1.1.101" where mac = "0010.A1AA.21CC"
Query OK, 1 row affected
Time: 0.003s

# 2022-12-15 06:40:35.615210
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

# 2022-12-15 06:40:52.465486
update switch set mngmt_ip = NULL where mac = "0010.A1AA.21CC"
Query OK, 1 row affected
Time: 0.003s

# 2022-12-15 06:40:54.454570
select * from switch
+----------------+----------+------------+-------------------+----------+-----------+
| mac            | hostname | model      | location          | mngmt_ip | mngmt_vid |
+----------------+----------+------------+-------------------+----------+-----------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str | <null>   | 255       |
| 0010.A1AA.21CC | sw101    | Cisco 3750 | London, Green Str | <null>   | 255       |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str | <null>   | 255       |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str | <null>   | 255       |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str | <null>   | 255       |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str | <null>   | 255       |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str | <null>   | 255       |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str | <null>   | 255       |
| 0110.A10A.C1CC | sw10     | 3750       | London, Green Str | <null>   | 255       |
+----------------+----------+------------+-------------------+----------+-----------+
9 rows in set
Time: 0.026s

# 2022-12-15 06:41:02.636951
update switch set hostname = "sw100" where mac = "0010.A1AA.21CC"
Query OK, 1 row affected
Time: 0.002s

# 2022-12-15 06:41:05.167313
select * from switch
+----------------+----------+------------+-------------------+----------+-----------+
| mac            | hostname | model      | location          | mngmt_ip | mngmt_vid |
+----------------+----------+------------+-------------------+----------+-----------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str | <null>   | 255       |
| 0010.A1AA.21CC | sw100    | Cisco 3750 | London, Green Str | <null>   | 255       |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str | <null>   | 255       |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str | <null>   | 255       |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str | <null>   | 255       |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str | <null>   | 255       |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str | <null>   | 255       |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str | <null>   | 255       |
| 0110.A10A.C1CC | sw10     | 3750       | London, Green Str | <null>   | 255       |
+----------------+----------+------------+-------------------+----------+-----------+
9 rows in set
Time: 0.021s

# 2022-12-15 06:41:41.846632
update switch set hostname = "sw101", mngmt_ip = "10.1.1.101" where mac = "0010.A1AA.21CC"
Query OK, 1 row affected
Time: 0.005s

# 2022-12-15 06:41:43.334984
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

# 2022-12-15 06:43:45.262046
.exit
Goodbye!
