username = input("Введите имя пользователя: ")
numbers = "0123456789"

passwd_wrong = True

# while passwd_wrong:
while passwd_wrong == True:
    password = input("Введите пароль: ")
    if len(password) < 8:
        print("Пароль слишком короткий")
    elif username.lower() in password.lower():
        print("В пароле содержится имя пользователя")
    elif len(set(password).intersection(set(numbers))) < 3:
        print("В пароле должно быть 3 уникальные цифры")
    else:
        print(f"Пароль для пользователя {username} установлен")
        passwd_wrong = False


print("#" * 40)
# passwd_correct = False
#
# while not passwd_correct:
#     password = input("Введите пароль: ")
#     if len(password) < 8:
#         print("Пароль слишком короткий")
#     elif username.lower() in password.lower():
#         print("В пароле содержится имя пользователя")
#     elif len(set(password).intersection(set(numbers))) < 3:
#         print("В пароле должно быть 3 уникальные цифры")
#     else:
#         print(f"Пароль для пользователя {username} установлен")
#         passwd_correct = True
