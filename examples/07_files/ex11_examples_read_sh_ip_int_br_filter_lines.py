from pprint import pprint

filename = "show_output/sh_ip_int_br.txt"
with open(filename) as f:
    for line in f:
        words = line.split()
        if len(words) >= 6 and words[1][0].isdigit():
            pprint(words)
