from pprint import pprint

def print_line(line_sym="=", length=40):
    """Функция вывод на stdout линию состоящую из line_sym * length"""
    print(str(line_sym) * length)


print_line()
print_line("-")
print_line("#", 50)
print_line(length=50)
print_line(length=50, line_sym="*")
# print_line(length=50, "*") # ERROR
print_line("#", length=50)
