"""CP1404 prac 9 band class"""


class Band:
    def __init__(self, band_name=""):
        """Construct a band object"""
        self.band_name = band_name
        self.members = []

    def __str__(self):
        """String form of band."""
        musician_details = ", ".join(
            f"{musician.name} ([{', '.join(str(instrument) for instrument in musician.instruments)}])"
            for musician in self.members)
        return f"{self.band_name} ({musician_details})"

    # def __repr__(self):
    #     """Return a string representation of a Band, showing the variables."""
    #     return str(vars(self))

    def add(self, musician):
        """Add a musician to the band"""
        self.members.append(musician)

    def play(self):
        """Return a string describing the band members and what they're playing."""
        if not self.members:
            return f"{self.band_name} has no musicians!"
        return "\n".join(musician.play() for musician in self.members)
