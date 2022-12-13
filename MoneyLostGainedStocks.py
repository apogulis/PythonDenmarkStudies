# This program calculates how much money
# did Joe gain or lost by buying stocks

# Share count, fee, bought and sold for
shares = 1000
buy_share = 32.87
broker = 0.02
sell_share = 33.92

# How much paid for stocks and to broker
paid = buy_share * shares
paid_broker = paid * broker

# How much sold stocks for and paid to broker
sold = sell_share * shares
sell_broker = sold * broker

# How much money gained or lost
income = sold - (paid + paid_broker + sell_broker)

print("Joe paid for the stocks ($):", format(paid, ',.2f'))
print("Commission when bought stocks ($):", format(paid_broker, '.2f'))
print("Joe sold stocks for ($):", format(sold, ',.2f'))
print("Commission when sold stocks ($):", format(sell_broker, '.2f'))
print("Profit ($):", format(income, '.2f'))
