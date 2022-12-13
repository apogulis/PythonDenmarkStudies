# This program calculates from mass in kilograms to weight in newtons

# Asks user to enter the value of mass and calculates weight

def main():
    mass = float(input("What is the mass in kilograms? "))
    coefficient = 9.8
    weight = mass * coefficient
    weight_check(weight)


# This function prints object weight on the screen and
# checks if the object is too heavy or too light

def weight_check(weight):
    if weight > 1000:
        print("The object is too heavy!")
    elif weight < 10:
        print("The object is too light!")
    else:
        print("Weight is", format(weight, '.2f'), "newtons.")


# Calling the main function
main()
