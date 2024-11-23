"""CP1404 prac 9 silver service taxi class test"""
from silver_service_taxi import SilverServiceTaxi

sst1 = SilverServiceTaxi("Hummer", 200, 4)
print(f"sst1: {sst1}")
sst2 = SilverServiceTaxi("Franklin", 200, 2)
print(f"sst2: {sst2}")
sst2.drive(18)
print(f"{sst2}, current fare: ${sst2.get_fare()}")