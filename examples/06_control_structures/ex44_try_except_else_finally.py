# -*- coding: utf-8 -*-

a = input("Введите первое число: ")
b = input("Введите второе число: ")
try:
    result = int(a) / int(b)
except (ValueError, ZeroDivisionError):
    print("Что-то пошло не так...")
else:
    print("Результат в квадрате: ", result ** 2)
finally:
    print("Вот и сказочке конец, а кто слушал - молодец.")
