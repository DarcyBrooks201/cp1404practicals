"""CP1404 prac 9 unreliable car class test"""

from unreliable_car import UnreliableCar

uc1 = UnreliableCar("Faith", 100, 50.5)
print(uc1)
for i in range(5):
    uc1.drive(20)
    print(uc1)
