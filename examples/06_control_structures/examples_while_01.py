num = ""

while not num.isdigit():
    num = input("Введите число: ")

print("Result", 100 * int(num))
