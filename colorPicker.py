import matplotlib.pyplot as plt


def colorPicker():
    # Create a list of 8 colors, evenly spaced between the two input colors
    while True:
        color1 = input("Enter the First RGB Color: ")
        color2 = input("Enter the Second RGB Color: ")
        color1 = "160,48,255" if color1 == "" else color1
        color2 = "98,0,255" if color2 == "" else color2
        print(color1 + " " + color2)
        colors = []
        for i in range(8):
            colors.append((int(color1[0]) + (i * (int(color2[0]) - int(color1[0])) / 7),
                           int(color1[1]) + (i * (int(color2[1]) - int(color1[1])) / 7),
                           int(color1[2]) + (i * (int(color2[2]) - int(color1[2])) / 7)))
            # Create a plot with the gradient colors
            plt.plot(colors[i])
        plt.show()
        confirm = input("Are you happy with this gradient? (Y/N)")

        if confirm.lower() == "y":
            plt.savefig("gradient.png")
            return colors[2]
        else:
            colors.clear()
