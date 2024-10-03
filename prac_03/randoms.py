"""CP1404 prac 3 randoms file"""
import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
# 5 is smalest, 20 is largest

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?
# 3 is smallest, 9 is largest, it could not produce a 4

# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
# 2.5 is smallest, 5.5 is largest

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))