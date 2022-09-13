words = ["one", "", "TWO", "test", "DATA"]

def lower(item):
    return item.lower()


print(sorted(words, key=lower))
