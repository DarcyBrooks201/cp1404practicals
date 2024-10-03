"""CP1404 Prac 3 Do-From_Scratch exercise files.py"""
# 1
name = input("name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()
#
# # 2
in_file = open("name.txt", "r")
line = in_file.readline()
name = line.strip("\n")
in_file.close()
print(f"Hi {name}!")

# 3
total_number = 0
with open("numbers.txt") as in_file:
    for i, line in enumerate(in_file):
        if i < 2:
            number = int(line.strip())
            total_number += number
print(total_number)

# 4
total_number = 0
with open("numbers.txt") as in_file:
    for line in in_file:
        number = int(line.strip())
        total_number += number
print(total_number)
