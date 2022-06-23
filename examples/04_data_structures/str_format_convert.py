from pprint import pprint
template = (
    "{:<8} {:<8} {:<8} {:<8}\n"
    "{:08b} {:08b} {:08b} {:08b}"
)

print(template.format(10, 1, 100, 5, 10, 1, 100, 5))

# names
template = (
    "{oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}\n"
    "{oct1:08b} {oct2:08b} {oct3:08b} {oct4:08b}"
)

print(template.format(oct1=10, oct2=1, oct3=100, oct4=5))

# numbers
template = (
    "{0:<8} {1:<8} {2:<8} {3:<8}\n"
    "{0:08b} {1:08b} {2:08b} {3:08b}"
)

print(template.format(10, 1, 100, 5))
#octets = [192, 168, 1, 1]
# print(template.format(octets))
#print(template.format(octets[0], octets[1], octets[2], octets[3]))

cfg = """
interface {0}
 ip address {1} 255.255.255.255

ip nat {0}
"""
