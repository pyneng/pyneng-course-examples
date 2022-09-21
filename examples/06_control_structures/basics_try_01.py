from pprint import pprint

items = ["1", "2", "test", "3"]
data = []

for i in items:
    pprint(i)
    value = int(i)
    data.append(value)
print(data)
