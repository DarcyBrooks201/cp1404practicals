def main():
    import random
    menu_choice = input("(N)ame, (P)rint, (S)ecret name, (Q)uit: ").upper()
    name = ""
    while menu_choice != "Q":
        if menu_choice == "N":
            name = get_name()
            menu_choice = input("(N)ame, (P)rint, (S)ecret name, (Q)uit: ").upper()
        elif menu_choice == "P":
            print_greeting(name)
            menu_choice = input("(N)ame, (P)rint, (S)ecret name, (Q)uit: ").upper()
        elif menu_choice == "S":
            random_number = random.randint(1, 5)
            secret_name = determine_secret_name(random_number)
            print(f"Your secret name is now {secret_name}")
            menu_choice = input("(N)ame, (P)rint, (S)ecret name, (Q)uit: ").upper()
        else:
            print("Error")
            menu_choice = input("(N)ame, (P)rint, (S)ecret name, (Q)uit ").upper()
    print(f"Goodbye")


def print_greeting(name):
    name_length = len(name)
    print("-" * name_length)
    print(name)
    print("-" * name_length)


def get_name():
    name = input("What is your name? ")
    while name == "":
        print("Error, name cannot be blank")
        name = input("What is your name? ")
    return name


def determine_secret_name(number):
    if number == 1:
        return "Alex"
    elif number == 2:
        return "Barry"
    elif number == 3:
        return "Charlotte"
    elif number == 4:
        return "Darius"
    else:
        return "Edgar"


main()
