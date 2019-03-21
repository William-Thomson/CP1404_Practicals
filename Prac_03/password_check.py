def main():
    password = get_password()
    print_asterisk(password)


def print_asterisk(password):
    print('*' * len(password))


def get_password():
    password = input('Enter password: ')
    while len(password) <= 3:
        password = input('Invalid password. Enter password: ')
    return password


main()
