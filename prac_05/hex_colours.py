"""
CP1404/CP5632 Practical
Hex_colours
"""

COLOUR_TO_HEX = {"acidgreen": "#b0bf1a", "alizarincrimson": "#e32636", "amethyst": "#9966cc", "apricot": "#fbceb1",
                 "aqua": "#00ffff", "aureolin": "#fdee00", "battleshipgray": "#848482", "gamboge": "#e49b0f",
                 "hotmagenta": "#ff1dce", "internationalorange": "#ff4f00"}
print(COLOUR_TO_HEX)

for COLOUR in COLOUR_TO_HEX:
    print(f"{COLOUR:3} is {COLOUR_TO_HEX[COLOUR]}")
colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_HEX[colour_name])
    except KeyError:
        print("Invalid short state")
    colour_name = input("Enter short state: ").lower()
