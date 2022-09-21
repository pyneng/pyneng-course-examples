from pprint import pprint

username = input("Введите имя пользователя: ")
password = input("Введите пароль: ")

numbers = set("0123456789")
correct_password = True

if len(password) < 8:
    print("Пароль слишком короткий")
    correct_password = False
if username.lower() in password.lower():
    print("В пароле содержится имя пользователя")
    correct_password = False
if len(numbers.intersection(set(password))) < 3:
    print("В пароле должны быть хотя 3 цифры")
    correct_password = False


if correct_password:
    print(f"Пароль для пользователя {username} установлен")
