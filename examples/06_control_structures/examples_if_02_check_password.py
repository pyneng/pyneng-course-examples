from pprint import pprint

username = input("Введите имя пользователя: ")
password = input("Введите пароль: ")
pprint(username)
pprint(password)

numbers = set("0123456789")

if len(password) < 8:
    print("Пароль слишком короткий")
elif username.lower() in password.lower():
    print("В пароле содержится имя пользователя")
elif len(numbers.intersection(set(password))) < 3:
    print("В пароле должны быть хотя 3 цифры")
else:
    print(f"Пароль для пользователя {username} установлен")
