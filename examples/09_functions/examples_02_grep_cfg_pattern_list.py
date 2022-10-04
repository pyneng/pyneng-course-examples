from pprint import pprint


def grep_cfg(filename, pattern_list):
    if type(pattern_list) == str:
        pattern_list = [pattern_list]
    lines = []
    with open(filename) as f:
        for line in f:
            for pattern in pattern_list:
                if pattern in line:
                    lines.append(line)
                    break
    return lines


result = grep_cfg("configs/config_r1.txt", ("interface", "ip address"))
pprint(result)
pprint(grep_cfg("configs/config_r5.txt", "alias"))


