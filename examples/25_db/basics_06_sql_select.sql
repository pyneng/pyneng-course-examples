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
Time: 0.037s

select mac from switch
+----------------+
| mac            |
+----------------+
| 0010.A1AA.21CC |
| 0010.A1AA.C1CC |
| 0020.A2AA.C2CC |
| 0030.A3AA.C3CC |
| 0040.A4AA.C4CC |
| 0050.A5AA.C5CC |
| 0060.A6AA.C6CC |
| 0070.A7AA.C7CC |
+----------------+
8 rows in set
Time: 0.023s

select mac, location, hostname from switch
+----------------+-------------------+----------+
| mac            | location          | hostname |
+----------------+-------------------+----------+
| 0010.A1AA.C1CC | London, Green Str | sw1      |
| 0010.A1AA.21CC | London, Green Str | <null>   |
| 0020.A2AA.C2CC | London, Green Str | sw2      |
| 0030.A3AA.C3CC | London, Green Str | sw3      |
| 0040.A4AA.C4CC | London, Green Str | sw4      |
| 0050.A5AA.C5CC | London, Green Str | sw5      |
| 0060.A6AA.C6CC | London, Green Str | sw6      |
| 0070.A7AA.C7CC | London, Green Str | sw7      |
+----------------+-------------------+----------+
8 rows in set
Time: 0.027s


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
Time: 0.018s

select * from switch where model = "Cisco 3850"
+----------------+----------+------------+-------------------+
| mac            | hostname | model      | location          |
+----------------+----------+------------+-------------------+
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str |
+----------------+----------+------------+-------------------+
3 rows in set
Time: 0.018s

select * from switch where model LIKE "Cisco 3850"
+----------------+----------+------------+-------------------+
| mac            | hostname | model      | location          |
+----------------+----------+------------+-------------------+
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str |
+----------------+----------+------------+-------------------+
3 rows in set
Time: 0.027s

select * from switch where model LIKE "%3750%"
+----------------+----------+------------+-------------------+
| mac            | hostname | model      | location          |
+----------------+----------+------------+-------------------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str |
| 0010.A1AA.21CC | <null>   | Cisco 3750 | London, Green Str |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str |
+----------------+----------+------------+-------------------+
4 rows in set
Time: 0.022s

select * from switch where model GLOB "*3750*"
+----------------+----------+------------+-------------------+
| mac            | hostname | model      | location          |
+----------------+----------+------------+-------------------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str |
| 0010.A1AA.21CC | <null>   | Cisco 3750 | London, Green Str |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str |
+----------------+----------+------------+-------------------+
4 rows in set
Time: 0.021s

select * from switch where model LIKE "Cisco 3850"
+----------------+----------+------------+-------------------+
| mac            | hostname | model      | location          |
+----------------+----------+------------+-------------------+
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str |
+----------------+----------+------------+-------------------+
3 rows in set
Time: 0.021s

select * from switch where model LIKE "%3750%"
+----------------+----------+------------+-------------------+
| mac            | hostname | model      | location          |
+----------------+----------+------------+-------------------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str |
| 0010.A1AA.21CC | <null>   | Cisco 3750 | London, Green Str |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str |
+----------------+----------+------------+-------------------+
4 rows in set
Time: 0.021s

select * from switch where model GLOB "*3750*"
+----------------+----------+------------+-------------------+
| mac            | hostname | model      | location          |
+----------------+----------+------------+-------------------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str |
| 0010.A1AA.21CC | <null>   | Cisco 3750 | London, Green Str |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str |
+----------------+----------+------------+-------------------+
4 rows in set
Time: 0.023s

select * from switch where model GLOB "*3[78]50*"
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
+----------------+----------+------------+-------------------+
7 rows in set
Time: 0.020s

select * from switch where model in ("Cisco 3750", "Cisco 3850")
+----------------+----------+------------+-------------------+
| mac            | hostname | model      | location          |
+----------------+----------+------------+-------------------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str |
| 0010.A1AA.21CC | <null>   | Cisco 3750 | London, Green Str |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str |
+----------------+----------+------------+-------------------+
6 rows in set
Time: 0.019s
