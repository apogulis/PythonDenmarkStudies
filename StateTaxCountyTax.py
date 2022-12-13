# This program calculates state and
# county tax from a purchase

# Asks for an amount
amount = float(input("What is the amount of a purchase? "))

# State tax 4% and county tax 2%
state_tax = 0.04
county_tax = 0.02

# Calculate, format and display

state_amount = amount * state_tax

county_amount = amount * county_tax

total_tax = state_amount + county_amount

total = amount + total_tax

print("Amount of a purchase:", format(amount, '.2f'))
print("State sales tax:", format(state_amount, '.2f'))
print("County sales tax:", format(county_amount, '.2f'))
print("Total sales tax:", format(total_tax, '.2f'))
print("Total Price:", format(total, '.2f'))
