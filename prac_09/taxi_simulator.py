"""CP1404 prac 9 taxi simulator"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_trip_cost = 0
    current_taxi = ""
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
            taxi_choice = int(input("Choose taxi: "))
            if taxi_choice > (len(taxis) - 1) or taxi_choice < 0:
                print("Invalid taxi choice")
            else:
                current_taxi = taxis[taxi_choice]
            print(f"Bill to date: ${total_trip_cost:.2f}")
            print_menu()
            menu_choice = input(">>> ").upper()
        elif menu_choice == "D":
            if current_taxi == "":
                print("You need to choose a taxi before you can drive")
            else:
                drive_distance = int(input("Drive how far? "))
                current_taxi.drive(drive_distance)
                current_fare = current_taxi.get_fare()
                total_trip_cost += current_fare
                print(f"Your {current_taxi.name} trip cost you ${current_fare:.2f}")
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
