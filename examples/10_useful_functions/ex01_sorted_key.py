list_of_words = ['one', 'two', 'list', ' ', 'dict', 'LIST', "ONE"]

print(sorted(list_of_words, key=len))
# [' ', 'one', 'two', 'ONE', 'list', 'dict', 'LIST']

def lower(x):
    return str(x).lower()

print(sorted(list_of_words, key=lower))
# [' ', 'dict', 'list', 'LIST', 'one', 'ONE', 'two']

