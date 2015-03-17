# Python Tip Calculator
# My first python script based on tip calculator on CodeAcademy
# 3/16/2015 - Jeremy Arntz

def calculateTip(subTotal, percentage):
	tip = float(subTotal) * percentage
	return "%.2f" % tip

def calculateTotal(subTotal, percentage):
	tipPercentage = float(percentage)/100
	tip           = calculateTip(subTotal, tipPercentage)
	total         = float(subTotal) + float(tip)
	return "%.2f" % float(total)

subTotal = raw_input("Enter the Total:")

if subTotal != '':
	fifteenPercent  = calculateTip(subTotal, 0.15)
	eighteenPercent = calculateTip(subTotal, 0.18)
	twentyPercent   = calculateTip(subTotal, 0.20)

	print "Tip:"
	print "15% - $"+fifteenPercent
	print "18% - $"+eighteenPercent
	print "20% - $"+twentyPercent

	tipPercentage = raw_input("Enter the tip Percentage:")

	if tipPercentage != '':
		billTotal = calculateTotal(subTotal, tipPercentage)
		print "Total with Tip $"+billTotal

		splitCheck = raw_input("Split check by:")

		if splitCheck != '':
			amountEach = float(billTotal)/float(splitCheck)
			splitAmount = "%.2f" % amountEach
			print "Everybody owes: $"+splitAmount