"""CP1404 Prac 3 Do-From_Scratch exercise files.py"""
# 1
name = input("name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2
in_file = open("name.txt", "r")
line = in_file.readline()
name = line.strip("\n")
in_file.close()
print(f"Hi {name}!")

# 3
with open("numbers.txt") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(number1 + number2)

# 4
total_number = 0
with open("numbers.txt") as in_file:
    for line in in_file:
        number = int(line.strip())
        total_number += number
print(total_number)
