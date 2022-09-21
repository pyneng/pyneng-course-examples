from pprint import pprint

username = input("Введите имя пользователя: ")
password = input("Введите пароль: ")

numbers = set("0123456789")

while (
    len(password) < 8
    or username.lower() in password.lower()
    or len(numbers.intersection(set(password))) < 3
):
    print("Пароль не прошел проверки")
    password = input("Введите пароль еще раз: ")


print(f"Пароль для пользователя {username} установлен")
