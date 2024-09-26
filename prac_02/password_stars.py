"""Create a string of stars based on length of password"""

def main():
    min_password_length = int(input("minimum length: "))
    password = get_password(min_password_length)
    print('*' * len(password))


def get_password(min_password_length):
    password = input("Password: ")
    while len(password) < min_password_length:
        print("Password must be longer")
        password = input("Password: ")
    return password


main()
