"""prac 6 guitar_test.py"""

from guitar import Guitar

g1 = Guitar("Gibson L-5 CES", 1922, 16035.4)
print(g1)
print(f"Guitar.get_age(g1) - Expected 100, got {Guitar.get_age(g1)}")
print(f"Guitar.is_vintage(g1) - Expected True, got {Guitar.is_vintage(g1)}")