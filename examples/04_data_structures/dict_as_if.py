

value = input("Что вывести? [ip/mac/mask]: ")
if value == "ip":
    print("10.1.1.1")
elif value == "mac":
    print("AAAA.BBBB.CCCC")
elif value == "mask":
    print("255.255.255.0")
else:
    print("такого значения нет")

choice = {
    "ip": "10.1.1.1",
    "mask": "255.255.255.0",
    "mac": "AAAA:BBBB:CCCC",
    "hostname": "sw1",
}
# print(choice[value])
print(choice.get(value, "такого значения нет"))
