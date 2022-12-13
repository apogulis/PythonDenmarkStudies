# This program converts Celsius to Fahrenheit

# Asks how many Celsius degrees
celsius = float(input("What is the temperature in Celsius? "))

# Converts, formats and displays Celsius to Fahrenheit
fahrenheit = (9 / 5) * celsius + 32

print(format(celsius, '.0f'), "Celsius is",
      format(fahrenheit, '.0f'), "Fahrenheit.")
