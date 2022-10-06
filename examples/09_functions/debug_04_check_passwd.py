from pprint import pprint

def password_check(user, passwd, min_len=8, spec_symbols=2):
    spec_symbols_str = "$#@%_+"
    pprint(locals())
    if len(passwd) < min_len:
        return False
    elif user.lower() in passwd.lower():
        return False
    elif len(set(spec_symbols_str) & set(passwd)) < 2:
        return False
    else:
        return True


username = "user1"
password = "1234567677"
result = password_check("user1", "passwo#rd+")
pprint(globals())
