# This program asks end user to enter digits and calculates their sum

def main():
    numbers = input('Enter a series of single-digit numbers with nothing separating them: ')

    # Created a variable to use as an accumulator
    total = 0
    # Calculate and display total from numbers
    for i in numbers:
        total += int(i)
    print(total)


# Calling the main function
main()
