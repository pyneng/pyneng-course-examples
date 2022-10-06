from pprint import pprint


def strip_and_lower(string):
    string = str(string)
    result = string.strip().lower()
    return result


def convert_str_list(lines):
    new_list = []
    for line in lines:
        new_line = strip_and_lower(line)
        new_list.append(new_line)
    return new_list


lines = [" line1\nTEST\nline2\n\n ", "LINE2 ", "  TESTLINE "]
result = convert_str_list(lines)
pprint(result)
