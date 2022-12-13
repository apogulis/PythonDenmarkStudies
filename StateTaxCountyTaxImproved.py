# This program calculates state and
# county tax from a purchase

def main():
    amount = float(input("What is the amount of a purchase? "))
    print("Amount of a purchase:", format(amount, '.2f'))
    calculate(amount)


def calculate(amount):
    state_tax = 0.04
    county_tax = 0.02
    state_amount = amount * state_tax
    county_amount = amount * county_tax
    total_tax = state_amount + county_amount
    total = amount + total_tax
    print("State sales tax:", format(state_amount, '.2f'))
    print("County sales tax:", format(county_amount, '.2f'))
    print("Total sales tax:", format(total_tax, '.2f'))
    print("Total Price:", format(total, '.2f'))


# Calculate, format and display

main()
