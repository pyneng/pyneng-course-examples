from pprint import pprint

num1 = 1
num2 = "1"

line = 'text\ttest'

cfg = '\ninterface Tunnel0\n ip address 10.10.10.1 255.255.255.0\n ip mtu 1416\n ip ospf hello-interval 5\n tunnel source FastEthernet1/0\n tunnel protection ipsec profile DMVPN\n'
tunnel = """
interface Tunnel0
 ip address 10.10.10.1 255.255.255.0
 ip mtu 1416
 ip ospf hello-interval 5
 tunnel source FastEthernet1/0
 tunnel protection ipsec profile DMVPN
"""
tunnel = (
    "\ninterface Tunnel0\n"
    " ip address 10.10.10.1 255.255.255.0\n"
    " ip mtu 1416\n"
    " ip ospf hello-interval 5\n"
    " tunnel source FastEthernet1/0\n"
    " tunnel protection ipsec profile DMVPN\n"
)
print(num1)
print(num2)
print(line)
print(tunnel)
print(cfg == tunnel)

pprint(num1)
pprint(num2)
pprint(line)
pprint(tunnel)
pprint(cfg == tunnel)
