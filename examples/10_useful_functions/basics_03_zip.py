# d_keys = ['hostname', 'location', 'vendor', 'model', 'ios', 'ip']
# d_values = ['london_r1', '21 New Globe Walk', 'Cisco', '4451', '15.4', '10.255.0.1']

ip_list = ["10.1.1.1", "10.2.2.2", "10.100.1.1", "1.100.100.1"]
ping_status = [True, True, False, False]

for index in range(len(ip_list)):
    print(f"{ip_list[index]:20} {ping_status[index]}")

print("=" * 40)

for ip, status in zip(ip_list, ping_status):
    print(f"{ip:20} {status}")

