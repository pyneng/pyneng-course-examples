access = {'0/12': 10, '0/14': 11, '0/16': 17, '0/17': 150}

for key in access:
    print(key, access[key])

for key in access.keys():
    value = access[key]
    print(key, value)

print(list(access.items()))
for key, value in access.items():
    print(key, value)
