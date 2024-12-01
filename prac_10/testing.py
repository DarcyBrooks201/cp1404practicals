"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    original = s * n
    answer = " ".join([s]*n)
    return answer


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) > length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"


    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # TODO: 2. write assert statements to show if Car sets the fuel correctly
    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    assert car.fuel == 0
    fuel = 10
    car = Car(fuel=fuel)
    assert car.fuel == fuel


run_tests()

# TODO: 3. Uncomment the following line and run the doctests
# (PyCharm may see your >>> doctest comments and run doctests anyway.)
# doctest.testmod()

# TODO: 4. Fix the failing is_long_word function
# (Don't change the tests, change the function!)

# TODO: 5. Write and test a function to format a phrase as a sentence,
# starting with a capital and ending with a single full stop.
# Important: start with a function header and just use pass as the body
# then add doctests for 3 tests:
#   'hello' -> 'Hello.'
#   'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more that you decide is a useful test.
# Run your doctests and watch the tests fail.
# Then write the body of the function so that the tests pass.