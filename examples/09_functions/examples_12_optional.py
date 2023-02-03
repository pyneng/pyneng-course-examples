

def password_check(user, passwd, min_len=8, check_user_in_passwd=False, unique_spec_sym=0):
    spec_sym_str = "$#@%_+"
    if len(passwd) < min_len:
        return False
    elif check_user_in_passwd and user.lower() in passwd.lower():
        return False
    elif unique_spec_sym and len(set(spec_sym_str) & set(passwd)) < unique_spec_sym:
        return False
    else:
        return True


print(password_check("user1", "12345678", min_len=6))
print(password_check("user1", "123456789", min_len=6, unique_spec_sym=2))
print(password_check("user1", "12345678$#@9", min_len=6, unique_spec_sym=2))

print(password_check("user1", "12aaUSER1aa89", min_len=6))
print(password_check("user1", "12aaUSER1aa89", min_len=6, check_user_in_passwd=True))
