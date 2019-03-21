def get_password():
    global password
    password = input('Enter password: ')
    while len(password) <= 3:
        password = input('Invalid password. Enter Password')
    return password


password = get_password()


def print_asterisk():
    print('*' * len(password))


print_asterisk()
