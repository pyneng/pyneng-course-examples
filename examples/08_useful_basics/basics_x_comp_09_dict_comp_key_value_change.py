from pprint import pprint

r1 = {
    "IOS": "15.4",
    "IP": "10.255.0.1",
    "hostname": "london_r1",
    "location": "21 New Globe Walk",
    "Model": "4451",
    "Vendor": "Cisco",
}

{
    "hostname": "london_r1",
    "ios": "15.4",
    "ip": "10.255.0.1",
    "location": "21 New Globe Walk",
    "model": "4451",
    "vendor": "Cisco",
}

device = {}
for key, value in r1.items():
    device[key.lower()] = value

pprint(device)


device = {key.lower(): value for key, value in r1.items()}
pprint(device)
