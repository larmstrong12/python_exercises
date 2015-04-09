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
barrels = (gallons / 19.5)
CO2 = round(gallons * 20.0, 2)
eth_Gas = round((gallons * 115000) / 75700, 2)
price = round(gallons * float(4), 2)

print "%.2f Gallons" % gallons
print "%.3f Liters" % liters
print "%.3f Barrels of Oil Required" % barrels
print "%.3f CO2 Produced in Pounds" % CO2
print "%.3f gallons of ethenol is equal to the same amount of energy in ethenol gas" % eth_Gas
print "$%.2f Per Gallon" % price