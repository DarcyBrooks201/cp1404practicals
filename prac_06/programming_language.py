"""prac 6 programming_language.py"""


class ProgrammingLanguage:
    def __init__(self, typing="Dynamic", reflection="Yes", year=1991):
        """Construct typing, reflection and year"""
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"