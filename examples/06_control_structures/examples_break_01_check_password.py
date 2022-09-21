username = input("Введите имя пользователя: ")
min_len = 8
numbers = "0123456789"


while True:
    password = input("Введите пароль: ")
    if len(password) < min_len:
        print("Пароль слишком короткий")
    elif username.lower() in password.lower():
        print("В пароле содержится имя пользователя")
    elif len(set(password).intersection(set(numbers))) < 3:
        print("В пароле должно быть 3 уникальные цифры")
    else:
        print(f"Пароль для пользователя {username} установлен")
        break
