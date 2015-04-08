num1 = raw_input("Enter first integer: ")
num2 = raw_input("Enter second integer: ")

num1 = int(num1)
num2 = int(num2)

numAdd = num1 + num2
numDiff = num1 - num2
numProd = num1 * num2
numQuot = num1 / num2
numRem = num1 % num2

print "The sum of " + str(num1) + " and " + str(num2) + " is " + str(numAdd)
print "The difference of " + str(num1) + " and " + str(num1) + " is " + str(numDiff)
print "The product of " + str(num1) + " and " + str(num2) + " is " + str(numProd)
print "The quotient of " + str(num1) + " and " + str(num2) + " is " + str(numQuot) + " with remainder " + str(numRem)