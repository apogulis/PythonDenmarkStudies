# This program calculates the minimum amount of money
# you should pay for property insurance

def main():
    cost = float(input("Enter the replacement cost: "))
    insurance_cost(cost)


def insurance_cost(cost):
    replace_amount = 0.8
    insurance = cost * replace_amount
    print("Minimum amount of insurance is",
          format(insurance, '.2f'), "EUR.")


# Calling the main function
main()
