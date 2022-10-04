
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


data = [
    ["user10", "sdld1235fj"],
    ["user20", "sdf####2245klfdj"],
    ["user30", "ssdkfjsus#%er3df"],
    ["user40", "sfjsus#%er3df"],
]

for username, password in data:
    passwd_status = password_check(username, password)
    print(f"{username=} {passwd_status=}")
