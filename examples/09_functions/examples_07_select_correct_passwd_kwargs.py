from pprint import pprint


def password_check(user, passwd, min_len=8, spec_symbols=2, numbers=3):
    spec_symbols_str = "$#@%_+"
    if len(passwd) < min_len:
        return False
    elif user.lower() in passwd.lower():
        return False
    elif len(set(spec_symbols_str) & set(passwd)) < spec_symbols:
        return False
    elif len(set("0123456789") & set(passwd)) < numbers:
        return False
    else:
        return True


def select_correct_password(user_passwd_list, **kwargs):
    print(f"{kwargs=}")
    password_ok = []
    password_not_ok = []
    for username, password in user_passwd_list:
        passwd_status = password_check(username, password, **kwargs)
        if passwd_status:
            password_ok.append([username, password])
        else:
            password_not_ok.append([username, password])
    return (password_ok, password_not_ok)


data = [
    ["user10", "sdld1235fj"],
    ["user20", "sdf####2245klfdj"],
    ["user30", "ssdkfjsus#%er3df"],
    ["user40", "sfjsus#%er3df"],
]

ok, not_ok = select_correct_password(data, min_len=6, test=2)
pprint(ok)
pprint(not_ok)
