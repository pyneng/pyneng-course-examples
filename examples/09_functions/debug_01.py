from pprint import pprint


def strip_and_lower(string):
    result = string.strip().lower()
    return result


item = " line1\nTEST\nline2\n\n "
new_item = strip_and_lower(100)
pprint(new_item)
