def validate_usr(username):
    import string
    flag = True
    a = string.ascii_lowercase + '_' + string.digits
    if len(username) in range(4, 17):
        for i in username:
            if i not in a:
                flag = False
    else:
        flag = False
    return flag


print(validate_usr('asddsa'))
