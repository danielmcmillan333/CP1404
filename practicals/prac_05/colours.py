
COLOUR_NAMES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "Blue1": "#0000ff", "Black":
           "#000000", "CadetBlue": "#5f9ea0", "Coral": "#ff7f50", "Cyan1": "#00ffff",
           "DarkGreen": "#006400", "DarkOrange": "#ff8c00", "FireBrick": "#b22222"}

colour = input("Please enter colour name: ")

while colour != "":
    if colour in COLOUR_NAMES:
        print("{}'s code is {}".format(colour, COLOUR_NAMES[colour]))
    else:
        print("Invalid colour.")
    colour = input("Please enter colour name: ")
