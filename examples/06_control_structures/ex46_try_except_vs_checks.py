# Вариант с try/except
a = input("Введите число: ")
b = input("Введите второе число: ")
try:
    result = int(a) / int(b)
except ValueError:
    print("Поддерживаются только числа")
except ZeroDivisionError:
    print("На ноль делить нельзя")
else:
    print(result)

# Аналогичное решение без try/except
a = input("Введите число: ")
b = input("Введите второе число: ")
if a.isdigit() and b.isdigit():
    if int(b) == 0:
        print("На ноль делить нельзя")
    else:
        print(int(a) / int(b))
else:
    print("Поддерживаются только числа")
