"""CP1404 prac 9 silver service taxi class"""
from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of taxi class"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness= 0.0):
        """Construct a silver_service_taxi object"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like car with flagfall"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"