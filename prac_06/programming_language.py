"""prac 6 programming_language.py"""


class ProgrammingLanguage:
    """Class ProgrammingLanguage that takes name, typing, reflection and year"""

    def __init__(self, name="", typing="Dynamic", reflection="Yes", year=1991):
        """Construct name, typing, reflection and year"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __repr__(self):
        """Return string of name, typing, reflection and year"""
        return f"{self.name}, {self.typing}, {self.reflection}, {self.year}"

    def is_dynamic(self):
        """Determine if a typing style is dynamic"""
        return self.typing == "Dynamic"
