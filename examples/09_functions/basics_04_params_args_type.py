


def check_passwd(user, passwd, min_len=8, unique_numbers=3):
    numbers = set("0123456789")
    if len(passwd) < min_len:
        return False
    elif user.lower() in passwd.lower():
        return False
    elif len(set(passwd) & numbers) < unique_numbers:
        return False
    else:
        return True

u = "user1"
p = "pasdweiruu39573498"
print(check_passwd("user1", "password234987234"))
print(check_passwd(u, p))
print(check_passwd("user1", "password234987234", 10, 2))
print(check_passwd("user1", "password234987234", min_len=10, unique_numbers=2))
print(check_passwd("user1", "password234987234", unique_numbers=2, min_len=10))
print(check_passwd(passwd="password234987234", user="user1", 10))
