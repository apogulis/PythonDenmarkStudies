# Asks user to enter the length and width of both rectangles

def main():
    rectangle1_length = float(input("Enter the LENGTH of the FIRST rectangle: "))
    rectangle1_width = float(input("Enter the WIDTH of the FIRST rectangle: "))
    rectangle2_length = float(input("Enter the LENGTH of the SECOND rectangle: "))
    rectangle2_width = float(input("Enter the WIDTH of the SECOND rectangle: "))

    rectangle1 = rectangle1_length * rectangle1_width
    rectangle2 = rectangle2_length * rectangle2_width

    rectangle_check(rectangle1, rectangle2)


# This function checks which rectangle has a greater area or are they equal

def rectangle_check(rectangle1, rectangle2):
    if rectangle1 > rectangle2:
        print("The FIRST rectangle has the greater area!")
    elif rectangle1 == rectangle2:
        print("Both rectangles are equal!")
    else:
        print("The SECOND rectangle has the greater area!")


# Calling the main function
main()
