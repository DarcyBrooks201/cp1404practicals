for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Question a
x = 10
for i in range(x+1):
    print(i*10)

# Question b
x = 20
for i in range(x):
    print(x)
    x -= 1

# Question c
number_of_stars = int(input("How many stars? "))
for i in range(number_of_stars):
    print("*", end="")

# Question d
number_of_stars = int(input("How many stars? "))
for i in range(number_of_stars):
    print("*" * (i+1))
