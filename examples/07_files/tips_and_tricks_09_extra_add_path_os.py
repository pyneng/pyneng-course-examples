from pprint import pprint
import os

path = "show_output"
files = ["sh_cdp_n_r1.txt", "sh_cdp_n_r2.txt", "sh_cdp_n_r3.txt", "sh_cdp_n_sw1.txt"]
print(files)

for file in files:
    full_filename = os.path.join(path, file)
    with open(full_filename, "r") as f:
        print(full_filename)
        for line in f:
            if "Eth" in line:
                print(line.rstrip())
