from pprint import pprint

with open("configs/config_r1.txt") as f:
    output = f.read()

result = {}
sections = output.split("!")
for section in sections:
    section = section.strip()
    # pprint(section, width=500)
    if section.startswith("interface"):
        print(section)
        print("-"*40)
        for line in section.split("\n"):
            if line.startswith("interface"):
                intf = line.split()[-1]
                if "ip address" not in section:
                    result[intf] = None
                    break
            elif line.startswith(" ip address"):
                ip = line.split()[-2]
                result[intf] = ip
pprint(result)
