# This program converts square feet to acres

# Asks how many square feet
square_feet = float(input("How many square feet is in a tract of land? "))

# 1 acre is 43,560 square feet
amount = 43560

# Calculates and displays acres
acres = square_feet / amount

print("There's", acres, "acres in the tract.")
