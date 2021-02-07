# loop/ program starts
while True:
    # Step 1 - retrieves user inputs
    itemPrice = float(input("What is the price of this item? "))
    percentageDiscount = float(input("What is the percentage discount? "))

    # Step 2 - processing calculation
    reducedPrice = itemPrice - itemPrice * percentageDiscount / 100

    # Step3: Generating the output
    print("The reduced price is " + str(reducedPrice))
    # asks user if they want to run the program again
    rerun = (input("Would you like to run this program again? 1 for Yes or 2 for No. "))
    if rerun != "1":
        print("Goodbye!")
        break
    # ends program if user does not want to try again
