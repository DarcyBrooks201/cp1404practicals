"""CP1404 prac 9 unreliable car class"""
from car import Car
import random

class UnreliableCar(Car):
    """Specialised version of Car class"""

    def __init__(self, name, fuel, reliability= 0.0):
        """Construct an unreliable car object"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()}, {self.reliability}% reliability"


    def drive(self, distance):
        """Drive the car a given distance, or until it runs out of fuel"""
        if random.randint(0, 100) < self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
        return distance
