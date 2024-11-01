"""prac 6 guitar.py
9:58 - 10:25
10:31 - 10:41
Expected 20 minutes, actually took 37
"""


class Guitar:
    """Guitar class that takes name, year and cost"""

    def __init__(self, name="", year=0, cost=0.0):
        """Construct object from name, year and cost"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """String version of Guitar parts like 'Gibson L-5 CES (1922) : $16,035.40' """
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Gets how old the guitar is based on current year"""
        current_year = 2022
        return int(current_year - self.year)

    def is_vintage(self):
        """Returns True if the guitar is over 50 years old"""
        age = Guitar.get_age(self)
        return age > 50


if __name__ == '__main__':
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
