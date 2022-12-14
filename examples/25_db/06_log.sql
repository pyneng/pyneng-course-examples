
# 2022-12-14 18:42:54.064290
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
+----------------+----------+------------+-------------------+
8 rows in set
Time: 0.036s

# 2022-12-14 18:42:59.994956
select * from switch group by model
+----------------+----------+------------+-------------------+
| mac            | hostname | model      | location          |
+----------------+----------+------------+-------------------+
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str |
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str |
+----------------+----------+------------+-------------------+
4 rows in set
Time: 0.024s

# 2022-12-14 18:44:44.252601
select * from switch order by hostname
+----------------+----------+------------+-------------------+
| mac            | hostname | model      | location          |
+----------------+----------+------------+-------------------+
| 0010.A1AA.21CC | <null>   | Cisco 3750 | London, Green Str |
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str |
+----------------+----------+------------+-------------------+
8 rows in set
Time: 0.019s

# 2022-12-14 18:44:49.535856
select * from switch order by hostname NULLS LAST
+----------------+----------+------------+-------------------+
| mac            | hostname | model      | location          |
+----------------+----------+------------+-------------------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str |
| 0010.A1AA.21CC | <null>   | Cisco 3750 | London, Green Str |
+----------------+----------+------------+-------------------+
8 rows in set
Time: 0.022s

# 2022-12-14 18:51:34.324579
select typeof(*) from switch 
wrong number of arguments to function typeof()

# 2022-12-14 18:51:43.375271
select typeof(hostname) from switch 
+------------------+
| typeof(hostname) |
+------------------+
| text             |
| null             |
| text             |
| text             |
| text             |
| text             |
| text             |
| text             |
+------------------+
8 rows in set
Time: 0.020s

# 2022-12-14 18:51:53.061757
select hostname, typeof(hostname) from switch 
+----------+------------------+
| hostname | typeof(hostname) |
+----------+------------------+
| sw1      | text             |
| <null>   | null             |
| sw2      | text             |
| sw3      | text             |
| sw4      | text             |
| sw5      | text             |
| sw6      | text             |
| sw7      | text             |
+----------+------------------+
8 rows in set
Time: 0.017s

# 2022-12-14 18:52:38.244697
insert into switch values ('0110.A10A.C1CC', 'sw10', 3750, 'London, Green Str')
Query OK, 1 row affected
Time: 0.003s

# 2022-12-14 18:52:40.537940
select hostname, typeof(hostname) from switch 
+----------+------------------+
| hostname | typeof(hostname) |
+----------+------------------+
| sw1      | text             |
| <null>   | null             |
| sw2      | text             |
| sw3      | text             |
| sw4      | text             |
| sw5      | text             |
| sw6      | text             |
| sw7      | text             |
| sw10     | text             |
+----------+------------------+
9 rows in set
Time: 0.020s

# 2022-12-14 18:52:48.070686
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
Time: 0.022s

# 2022-12-14 18:53:03.000135
select model, typeof(model) from switch 
+------------+---------------+
| model      | typeof(model) |
+------------+---------------+
| Cisco 3750 | text          |
| Cisco 3750 | text          |
| Cisco 3850 | text          |
| Cisco 3750 | text          |
| Cisco 3850 | text          |
| Cisco 3850 | text          |
| C3750      | text          |
| Cisco 3650 | text          |
| 3750       | text          |
+------------+---------------+
9 rows in set
Time: 0.020s

# 2022-12-14 18:53:23.814589
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
Time: 0.024s

# 2022-12-14 18:54:10.479156
.exit
Goodbye!
