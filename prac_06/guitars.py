"""Prac 6 guitars.py"""
from guitar import Guitar

guitars = []
# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
print("My guitars!")
new_guitar_name = input("Name: ")
while new_guitar_name != "":
    new_guitar_year = int(input("Year: "))
    new_guitar_cost = float(input("Cost: $"))
    new_guitar = Guitar(new_guitar_name, new_guitar_year, new_guitar_cost)
    guitars.append(new_guitar)
    print(f"{Guitar.__str__(new_guitar)} added.")
    new_guitar_name = input("Name: ")
print()
print("... snip ...")
print()
print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    if Guitar.is_vintage(guitar):
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
