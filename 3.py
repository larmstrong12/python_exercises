MPH = raw_input("Please enter a speed in MPH: ")

MPH = float(MPH)

meters_hour = MPH * 1609.34
yards_hour = MPH * 1760

barley_corn = (meters_hour * 117.647) * 24
furlong_fornight = (yards_hour / 220) * (24 * 14)
mach = MPH / 761.207051
light_speed = meters_hour / (299792458 * 60 * 60)


print "The original speed in MPH is: %.02f" % MPH
print "Converted to barleycorn/day is: %f" % barley_corn
print "Converted to furlongs/fornight is: %f" % furlong_fornight
print "Converted to Mach number is: %f" % mach
print "Converted to the percentage of the speed of light is: %f" % light_speed
print "Thanks for playing!"