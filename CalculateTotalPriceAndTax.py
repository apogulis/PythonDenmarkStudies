# This program asks price of 5 items and calculates
# subtotal price, sales tax and total price

# Asks price of 5 items
item1_price = float(input("What is the price of the first item? "))
item2_price = float(input("What is the price of the second item? "))
item3_price = float(input("What is the price of the third item? "))
item4_price = float(input("What is the price of the fourth item? "))
item5_price = float(input("What is the price of the fifth item? "))

# Tax is 6%
tax = 0.06

# Calculate and display
subtotal = item1_price + item2_price + item3_price + item4_price + item5_price

sales_tax = subtotal * tax

total = subtotal + sales_tax

print("Subtotal Price:", subtotal, "EUR")
print("Sales Tax:", sales_tax, "EUR")
print("Total Price:", total, "EUR")
