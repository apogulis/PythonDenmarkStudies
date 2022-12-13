# This program converts numbers to roman numbers

# Asks user to enter a number

def main():
    insert_number = float(input("Enter a number from 1 to 10: "))
    number_check(insert_number)


# This function converts to roman numbers or displays error message

def number_check(insert_number):
    if insert_number == 1:
        print("I")
    elif insert_number == 2:
        print("II")
    elif insert_number == 3:
        print("III")
    elif insert_number == 4:
        print("IV")
    elif insert_number == 5:
        print("V")
    elif insert_number == 6:
        print("VI")
    elif insert_number == 7:
        print("VII")
    elif insert_number == 8:
        print("VIII")
    elif insert_number == 9:
        print("IX")
    elif insert_number == 10:
        print("X")
    else:
        print("Error! Your number should be from 1 to 10!")


# Calling the main function
main()
