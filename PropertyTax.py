# This program calculates assessment value of
# the property and property tax

def main():
    property_value = float(input("Enter property value: "))
    calculate(property_value)


def calculate(property_value):
    assessment_percentage = 0.6
    property_percentage = 0.0064
    assessment_value = property_value * assessment_percentage
    property_tax = assessment_value * property_percentage
    print("Assessment value is ",
          format(assessment_value, '.2f'), "EUR.")
    print("Property tax is ",
          format(property_tax, '.2f'), "EUR.")


# Calling the main function
main()
