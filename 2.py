def get_input(message):
    try:
        user_input = str(input(message))
        if user_input.isdigit() and user_input is not "0":
            return user_input
        elif user_input is "0":
            print("Cannot be 0!")
        return None
    except NameError:
        print("That doesn't seem to be a number.")
        return None

gallons = None

while gallons is None:
    gallons = get_input("Please input the number of gallons: ")
    if gallons is not None:
        gallons = float(gallons)

gallons = float(gallons)

liters = gallons * 3.7854
barrels = round(gallons / 19.5 ,2)
CO2 = round(gallons * 20.0, 2)
eth_Gas = round((gallons * 115000) / 75700, 2)
price = round(gallons * float(4), 2)

print "{} Gallons".format(gallons)
print "{} Liters".format(liters)
print "{} Barrels of Oil Required".format(barrels)
print "{} CO2 Produced in Pounds".format(CO2)
print "{} gallons of ethenol is equivalent to energy amount in ethenol gas".format(eth_Gas)
print "${} Per Gallon".format(price)