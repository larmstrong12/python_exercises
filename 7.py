cities = {
    "Boston": "0 C",
    "Boise": "48 F",
    "Phoenix": "85 F",
    "Miami": "40 C",
    "Riverside": "30 C",
    "Baltimore": "32 F",
}
print

for key, value in cities.iteritems():
    if value[-1] == "C":
        value = value[:-2]
        print "In {} it is {} degrees Celsius" .format(key, value)
        print "\twhich is equivalent to {} in Fahrenheit\n".format((int(value) * 1.8) + 32)
        # value * 2.6 to get fahrenheit
    else:
        value = value[:-2]
        print "In {} it is {} degrees Fahrenheit" .format(key, value)
        print "\twhich is equivalent to {} in Celsius\n".format((int(value) - 32) / 1.8)
        # value / 2.6 to get celsius