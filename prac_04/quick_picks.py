"""CP1404 prac 4 quick_picks file"""

import random
NUMBER_OF_RANDOM_NUMBERS = 6
MINIMUM_RANDOM = 1
MAXIMUM_RANDOM = 45
number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    random_numbers = []
    while len(random_numbers) < NUMBER_OF_RANDOM_NUMBERS:
        random_numbers.append(random.randint(MINIMUM_RANDOM, MAXIMUM_RANDOM))
    random_numbers.sort()
    print(random_numbers)

