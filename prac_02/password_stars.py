min_password_length = int(input("minimum length: "))
password = input("Password: ")
while len(password) < min_password_length:
    print("Password must be longer")
    password = input("Password: ")
print('*' * len(password))