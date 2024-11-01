"""prac 6 guitar.py
9:58 -
Expected 20 minutes, actually
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
        return int(2022 - self.year)

    def is_vintage(self):
        """Returns True if the guitar is over 50 years old"""
        age = Guitar.get_age(self)
        return age > 50


