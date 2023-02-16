project2_package/
├── __init__.py
├── connect.py
├── configs
│   ├── cisco.py
│   └── __init__.py
└── parse
    ├── cisco.py
    ├── __init__.py
    └── juniper.py

# __init__.py
from project2_package.connect import *
from project2_package.parse import cisco
from project2_package.parse import juniper as parse_juniper
from project2_package.configs.cisco import *

# connect.py
print("Import connect.py")


def connect_ssh(ip):
    print("Connect SSH to {}".format(ip))


def connect_telnet(ip):
    print("Connect Telnet to {}".format(ip))

# configs/cisco.py
print("Import configs/cisco.py")

basic_cfg = """
service timestamps debug datetime msec localtime show-timezone year
service timestamps log datetime msec localtime show-timezone year
"""

lines_cfg = """
!
line con 0
"""

# parse/cisco.py
print("Import parse/cisco.py")

def parse_with_re(command):
    print("Parse command {} with regex".format(command))

def parse_with_textfsm(command):
    print("Parse command {} with texfsm".format(command))

# parse/juniper.py
print("Import parse/juniper.py")

def parse_with_re(command, regex):
    print("Parse command {} with regex {}".format(command, regex))

def parse_with_textfsm(command, template):
    print("Parse command {} with texfsm {}".format(command, template))

