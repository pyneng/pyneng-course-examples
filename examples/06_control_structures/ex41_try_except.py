# -*- coding: utf-8 -*-

a = input("Введите первое число: ")
b = input("Введите второе число: ")

try:
    result = int(a) / int(b)
except ValueError:
    print("Пожалуйста, вводите только числа")
except ZeroDivisionError:
    print("На ноль делить нельзя")
else:
    print("Результат: ", result)
finally:
    print("выполняется всегда")
