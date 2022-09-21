n1 = input("Введите первое число: ")
n2 = input("Введите второе число: ")

try:
    n1 = int(n1)
    n2 = int(n2)
except ValueError as error:
    print("Что-то не так", error)
else:
    result = n1 / n2
    print("Результат", result)
finally:
    print("The End")
