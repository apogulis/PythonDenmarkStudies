# This program asks for 2 primary colors and then shows
# what color we will get if we mix both of them together

# Asks user to enter 2 primary colors

def main():
    first_color = input("Enter FIRST primary color (Red, Blue or Yellow): ")
    second_color = input("Enter SECOND primary color (Red, Blue or Yellow): ")
    color_check(first_color, second_color)


# This function checks both colors and displays the mixed, secondary color

def color_check(first_color, second_color):
    if first_color == second_color:
        print("Colors are the same!")
    elif first_color == "Red" and second_color == "Blue" or first_color == "Blue" and second_color == "Red":
        print("You get PURPLE!")
    elif first_color == "Red" and second_color == "Yellow" or first_color == "Yellow" and second_color == "Red":
        print("You get ORANGE!")
    elif first_color == "Blue" and second_color == "Yellow" or first_color == "Yellow" and second_color == "Blue":
        print("You get GREEN!")
    else:
        print("Please, pick RED, BLUE or YELLOW!")


# Calling the main function
main()
