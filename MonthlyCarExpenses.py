# This program calculates monthly and annual automobile cost

def main():
    loan_payment = float(input("Enter monthly loan payment expenses: "))
    insurance = float(input("Enter monthly insurance expenses: "))
    gas = float(input("Enter monthly gas expenses: "))
    oil = float(input("Enter monthly oil expenses: "))
    tires = float(input("Enter monthly tire expenses: "))
    maintenance = float(input("Enter monthly maintenance expenses: "))
    calculate(loan_payment, insurance, gas, oil, tires, maintenance)


def calculate(loan_payment, insurance, gas, oil, tires, maintenance):
    monthly_exp = loan_payment + insurance + gas + oil + tires + maintenance
    annual_exp = monthly_exp * 12
    print("Your monthly expenses:", format(monthly_exp, '.2f'), "EUR.")
    print("Your annual expenses:", format(annual_exp, '.2f'), "EUR.")


# Calling the main function
main()
