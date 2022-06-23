from pprint import pprint

with open("show_output/sh_ip_int_br.txt") as src:
    filtered_lines = []
    for line in src:
        if line.count("up") == 2:
            pprint(line)
            filtered_lines.append(line)
pprint(filtered_lines)

with open("result_1.txt", "w") as dst:
    dst.writelines(filtered_lines)
