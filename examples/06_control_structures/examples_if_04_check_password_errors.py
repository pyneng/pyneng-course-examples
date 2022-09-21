from pprint import pprint

username = input("Введите имя пользователя: ")
password = input("Введите пароль: ")

numbers = set("0123456789")
errors = ""

if len(password) < 8:
    errors = errors + "Пароль слишком короткий\n"
    # errors += "Пароль слишком короткий"
if username.lower() in password.lower():
    errors += "В пароле содержится имя пользователя\n"
if len(numbers.intersection(set(password))) < 3:
    errors += "В пароле должны быть хотя 3 цифры\n"


if errors:
    print(errors)
else:
    print(f"Пароль для пользователя {username} установлен")
