device = ["10.1.1.1", "london_R1", "Cisco"]

index = 0

for param in device:
    if param == "Cisco":
        device[index] = param.upper()
    index += 1


device
['10.1.1.1', 'london_R1', 'CISCO']

list(enumerate(device))
[(0, '10.1.1.1'), (1, 'london_R1'), (2, 'CISCO')]

device = ["10.1.1.1", "london_R1", "Cisco"]

for index, param in enumerate(device):
    if param == "Cisco":
        device[index] = param.upper()

print(device)
