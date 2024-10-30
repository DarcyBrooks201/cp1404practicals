import random


def print_grid(length, width):
    # Option 1
    print(f"{'*' * width}\n" * length)
    # Option 2
    # for i in range(length):
    #     print("*" * width)


length = int(input("Length: "))
width = random.randint(1, length)
area = length * width
print(f"Area of {length} x {width} is {area}.")
print_grid(length, width)
