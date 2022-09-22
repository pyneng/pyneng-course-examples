london = {
    "name": "London1",
    "location": "London Str",
    "vendor": "Cisco",
    "ip": "10.1.1.1",
}

for key in london.copy():
    if key == "location":
        del london[key]
print(london)
# del london["location"]
