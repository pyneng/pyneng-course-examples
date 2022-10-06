from pprint import pprint

def strip_and_lower(string):
    string = str(string)
    result = string.strip().lower()
    return result


lines = [" line1\nTEST\nline2\n\n ", "LINE2 ", "  TESTLINE "]
for line in lines:
    new_line = strip_and_lower(line)
    pprint(new_line)
