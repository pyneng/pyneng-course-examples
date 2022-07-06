inv_data = [
    ("London_PE1", "10.1.1.1", "Cisco"),
    ("London_PE2", "10.2.2.2", "Cisco"),
    ("London_PE3", "10.3.3.3", "Cisco"),
]

for host, *rest in inv_data:
    print(host, rest)
