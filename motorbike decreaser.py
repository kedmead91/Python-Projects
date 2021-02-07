while True:
    years = float(input("How many years have you had your motorbike? "))
    motorbikeStartPrice = 2000
    percentageDiscount = float(10)
    reducedPrice = motorbikeStartPrice - motorbikeStartPrice * years * percentageDiscount / 100
    print("In the next " + str(years) + " year/s, your motorbike will be worth " + str(reducedPrice) + " pounds.")
    rerun = input("Would you like to run this program again? 1 for Yes or 2 for No. ")

    if rerun != "1":
        break
