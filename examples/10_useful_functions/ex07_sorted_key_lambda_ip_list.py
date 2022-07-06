from pprint import pprint

data = ["test", "TEXT", "ONE", "one"]

def lower(x):
    return str(x).lower()

lambda x: str(x).lower()

print(sorted(data, key=lower))
print(sorted(
    data, key=lambda x: str(x).lower()
))

