#!/usr/bin/env python
from pprint import pprint

access_str = """
switchport mode access
switchport access vlan {}
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
"""

print(access_str.format(42))
# pprint(access_str)

