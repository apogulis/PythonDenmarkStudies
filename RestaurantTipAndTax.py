# This program calculates tip and tax
# at the restaurant

# Asks how much food costs
amount = float(input("What is the charge for the food? "))

# Tip 15% and sales tax 7%
tip = 0.15
tax = 0.07

# Calculate, format and display

tip_total = amount * tip

tax_total = amount * tax

total = amount + tip_total + tax_total

print("Charge for the food:", format(amount, '.2f'))
print("Tip", format(tip_total, '.2f'))
print("Sales tax:", format(tax_total, '.2f'))
print("Total price:", format(total, '.2f'))
