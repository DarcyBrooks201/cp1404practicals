"""CP1404 prac 9 taxi simulator"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_trip_cost = 0
    print("Let's drive!")
    print_menu()
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "C":
            print("Taxis available: ")
            taxi_number = 0
            for taxi in taxis:
                print(f"{taxi_number} - {taxi}")
                taxi_number += 1

            print(f"Bill to date: ${total_trip_cost:.2f}")
            print_menu()
            menu_choice = input(">>> ").upper()
        elif menu_choice == "D":
            pass
            print(f"Bill to date: ${total_trip_cost:.2f}")
            print_menu()
            menu_choice = input(">>> ").upper()
        else:
            print("Invalid option")
            print(f"Bill to date: ${total_trip_cost:.2f}")
            print_menu()
            menu_choice = input(">>> ").upper()
    print(f"Total trip cost: ${total_trip_cost:.2f}")
    # TODO finish this print
    print(f"Taxi's are now...")


def print_menu():
    """Print the menu options"""
    print(f"q)uit, c)hoose taxi, d)rive")


main()
