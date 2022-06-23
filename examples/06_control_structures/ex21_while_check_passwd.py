username = input("Введите имя пользователя: ")
password = input("Введите пароль: ")

min_len = 8
numbers = "0123456789"

while (
    len(password) < 8
    or username.lower() in password.lower()
    or len(set("0123456789") & set(password)) < 3
):
    print(f"Пароль для {username} не прошел проверки")
    password = input("Введите пароль еще раз: ")

print(f"Пароль для {username} прошел все проверки")

# while not (
#     len(password) >= 8
#     and username.lower() not in password.lower()
#     and len(set("0123456789") & set(password)) >= 3
# ):
#     print(f"Пароль для {username} не прошел проверки")
#     password = input("Введите пароль еще раз: ")
#
# print(f"Пароль для {username} прошел все проверки")
