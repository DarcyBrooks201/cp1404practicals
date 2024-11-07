"""prac 7 myguitars.py"""

from guitar import Guitar


def main():
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        new_guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(new_guitar)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


main()
