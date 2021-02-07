# Program shows 10% decrease in motorbike value depending on how many years user has had it
while True:
    # asks user how many years they have had their motorbike
    years = float(input("How many years have you had your motorbike? "))
    # motobikes starting price
    motorbikeStartPrice = 2000
    # percentage that will be deducted
    percentageDiscount = float(10)
    # calculates decreased total
    reducedPrice = motorbikeStartPrice - motorbikeStartPrice * years * percentageDiscount / 100
    # prints how long user has had motorbike and the amount it is worth
    print("You have had your motorbike " + str(years) + " year/s, it is now worth " + str(reducedPrice) + " pounds.")
    # asks user if they want to rerun program to check other years totals
    rerun = input("Would you like to run this program again? 1 for Yes or 2 for No. ")

    if rerun != "1":
        break
# loop ends when user inputs 2
