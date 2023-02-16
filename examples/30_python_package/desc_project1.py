# project1_basics/
# ├── connect.py
# ├── exceptions.py
# ├── __init__.py
# └── utils.py

# connect.py
print("Import connect.py")

def connect_ssh(ip):
    print(f"Connect SSH to {ip}")

def connect_telnet(ip):
    print(f"Connect Telnet to {ip}")


# exceptions.py
class MyException(Exception):
    pass


# utils.py
def some_func():
    pass


# __init__.py
from project1_basics.connect import *

