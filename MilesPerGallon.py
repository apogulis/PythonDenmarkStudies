# This program calculates miles per gallon

# Asks miles driven and gallons used
miles_driven = float(input("How many miles driven? "))
gallons_used = float(input("How many gallons of gas used? "))

# Calculate, format and display miles per gallon
mpg = miles_driven / gallons_used

print("Car has", format(mpg, '.2f'), "miles per gallon (MPG).")
