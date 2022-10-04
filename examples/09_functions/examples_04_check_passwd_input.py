
def password_check(user, passwd, min_len=8, spec_symbols=2):
    spec_symbols_str = "$#@%_+"
    if len(passwd) < min_len:
        return False
    elif user.lower() in passwd.lower():
        return False
    elif len(set(spec_symbols_str) & set(passwd)) < 2:
        return False
    else:
        return True


def password_check_input(min_len=8, spec_symbols=2):
    user = input("Введите имя пользователя: ")
    passwd = input("Введите пароль: ")
    correct_password = password_check(user, passwd, min_len, spec_symbols)
    if correct_password:
        return user, passwd
    else:
        raise ValueError("Пароль не прошел проверки")

try:
    user, passwd = password_check_input()
except ValueError:
    pass
else:
    pass
