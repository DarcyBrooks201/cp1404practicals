"""prac 7 myguitars.py"""

from guitar import Guitar


def main():
    guitars = []
    load_guitars(guitars)
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    new_guitar_name = input("Name: ")
    while new_guitar_name != "":
        new_guitar_year = int(input("Year: "))
        new_guitar_cost = float(input("Cost: $"))
        new_guitar = Guitar(new_guitar_name, new_guitar_year, new_guitar_cost)
        guitars.append(new_guitar)
        print(f"{Guitar.__str__(new_guitar)} added.")
        new_guitar_name = input("Name: ")
    write_guitars(guitars)
    print("Done")


def load_guitars(guitars):
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        new_guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(new_guitar)
    in_file.close()


def write_guitars(guitars):
    out_file = open('guitars.csv', 'w')
    for guitar in guitars:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()
