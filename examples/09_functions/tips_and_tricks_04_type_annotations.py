

def check_passwd(username: str, password: str, min_length: int = 8) -> bool:
    if len(password) < min_length:
        print("Пароль слишком короткий")
        return False
    elif check_username and username in password:
        print("Пароль содержит имя пользователя")
        return False
    else:
        print(f"Пароль для пользователя {username} прошел все проверки")
        return True
