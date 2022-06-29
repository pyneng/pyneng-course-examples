from pprint import pprint


path = "show_output"
files = ["sh_cdp_n_r1.txt", "sh_cdp_n_r2.txt", "sh_cdp_n_r3.txt", "sh_cdp_n_sw1.txt"]

for file in files:
    full_filename = f"{path}/{file}"
    pprint(full_filename)
    with open(full_filename, "r") as f:
        for line in f:
            if "Eth" in line:
                pprint(line.rstrip())
