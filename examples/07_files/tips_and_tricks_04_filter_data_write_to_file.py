from pprint import pprint

file = "show_output/sh_ip_int_br.txt"

with open(file) as src:
    with open("result_1.txt", "w") as dst:
        for line in src:
            if line.count("up") == 2:
                dst.write(line)


