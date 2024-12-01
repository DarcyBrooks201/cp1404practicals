"""CP1404 prac 9 taxi class test"""
from taxi import Taxi

t1 = Taxi("Prius 1", 100)
t1.drive(40)
print(f"{t1}, current fare: ${t1.get_fare():.2f}")
t1.start_fare()
t1.drive(100)
print(f"{t1}, current fare: ${t1.get_fare():.2f}")
