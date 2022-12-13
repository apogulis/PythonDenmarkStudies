# This program converts kilometers to miles

# Asks for kilometers, converts to miles and displays on screen

def main():
    kilometers = float(input("How many kilometers? "))
    miles_converter(kilometers)


def miles_converter(kilometers):
    miles_value = 0.6214
    miles = kilometers * miles_value
    print(format(kilometers, '.2f'), "kilometers is ",
          format(miles, '.2f'), "miles.")


# Calling the main function
main()
