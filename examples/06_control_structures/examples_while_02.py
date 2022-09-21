num = ""

attempt = 1
while attempt <= 5 and not num.isdigit():
    print(attempt)
    num = input("Введите число: ")
    attempt += 1

if num.isdigit():
    print("Result", 100 * int(num))
