n1 = input("Введите первое число: ")
n2 = input("Введите второе число: ")

try:
    result = int(n1) / int(n2)
except (ValueError, ZeroDivisionError) as error:
    print("Что-то не так", error)
else:
    print("Результат", result)
finally:
    print("The End")
