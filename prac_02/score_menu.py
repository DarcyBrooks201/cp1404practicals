"""cp1404 prac 2 - creating a menu"""


def main():
    menu = """(G)et a valid score
(P)rint result 
(S)how stars (this should print as many stars as the score)
(Q)uit"""
    score = get_valid_score()
    print(menu)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "G":
            score = get_valid_score()
            print(menu)
            menu_choice = input(">>> ").upper()
        elif menu_choice == "P":
            grade = determine_grade(score)
            print(grade)
            print(menu)
            menu_choice = input(">>> ").upper()
        elif menu_choice == "S":
            print('*' * len(score))
            print(menu)
            menu_choice = input(">>> ").upper()
        else:
            print("error")
            print(menu)
            menu_choice = input(">>> ").upper()
    print("Goodbye")


def get_valid_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def determine_grade(score):
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
