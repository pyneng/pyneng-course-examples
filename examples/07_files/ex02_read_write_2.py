from pprint import pprint

with open("show_output/sh_ip_int_br.txt") as src:
    with open("result_1.txt", "w") as dst:
        for line in src:
            if line.count("up") == 2:
                pprint(line)
                dst.write(line)

file_src = "show_output/sh_ip_int_br.txt"
file_dst = "result_1.txt"
with open(file_src) as src, open(file_dst, "w") as dst:
    for line in src:
        if line.count("up") == 2:
            pprint(line)
            dst.write(line)
