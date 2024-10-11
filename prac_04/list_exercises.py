"""Cp1404 Prac 4 lists_exercises file"""

numbers = []
total = 0
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)
print(f"The first number is {numbers[0]} ")
print(f"The last number is {numbers[-1]} ")
print(f"The smallest number is {min(numbers)} ")
print(f"The largest number is {max(numbers)} ")
for number in numbers:
    total += number
average = total / len(numbers)
print(f"The average of the numbers is {average:.2} ")