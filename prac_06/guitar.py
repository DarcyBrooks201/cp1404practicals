"""prac 6 guitar.py
9:58 -
Expected 20 minutes, actually
"""

class Guitar:
    """Guitar class that takes name, year and cost"""

    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost