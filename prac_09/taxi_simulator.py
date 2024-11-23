"""CP1404 prac 9 taxi simulator"""

def main():
    print("Let's drive!")
    print_menu()
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "C":
            pass
            print_menu()
            menu_choice = input(">>> ").upper()
        elif menu_choice == "D":
            pass
            print_menu()
            menu_choice = input(">>> ").upper()
        else:
            print("Invalid menu option")
            print_menu()
            menu_choice = input(">>> ").upper()
    print(f"Total trip cost: ${total_trip_cost:.2f}")
    #TODO finish this print
    print(f"Taxi's are now...")


def print_menu():
    """Print the menu options"""
    print(f"q)uit, c)hoose taxi, d)rive")


main()