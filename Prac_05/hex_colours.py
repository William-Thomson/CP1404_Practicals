HEX_COLOURS = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine1": "#7fffd4", "azure1": "#f0ffff",
               "beige": "#f5f5dc", "bisque1": "#ffe4c4", "black": "#000000", "BlanchedAlmond": "#ffebcd",
               "blue1": "#0000ff", "BlueViolet": "#8a2be2", "brown": "#a52a2a"}

colour = input("Enter colour name: ")
while colour != "":
    if colour in HEX_COLOURS:
        print(colour, "is", HEX_COLOURS[colour])
    else:
        print("invalid colour")
    colour = input("Enter colour name: ")
