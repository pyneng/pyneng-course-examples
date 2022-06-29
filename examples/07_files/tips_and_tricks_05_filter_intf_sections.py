from pprint import pprint

src_file = "configs/config_r1.txt"
dst_file = "result_1.txt"

with open(src_file) as src, open(dst_file, "w") as dst:
    write_line = False
    for line in src:
        if line.startswith("interface"):
            dst.write(line)
            write_line = True
        elif line.startswith(" "):
            if write_line:
                dst.write(line)
        else:
            write_line = False
