# Beginning & Defining of function
def favourite_meal():
    # requesting user input
    user = input("Hello what is your name? ")
    # prints hello & users name
    print("Hello " + user)
    print("Can I ask you questions about your favourite meal?")
    # asks user if they want to take part
    yes_no = input("Please press 1 for Yes and 2 for No ")
    # if 1 then the function goes ahead if 2 then function will end
    if yes_no == '2':
        quit("Okay, maybe another time")
    else:
        # asks first question (starter)
        print("Okay thanks, First Question: ")
        starter = input("What is your favourite starter? ")
        # asks second question (main course)
        main_course = input("What is your favourite main course? ")
        # asks third question (dessert)
        dessert = input("What is your favourite dessert? ")
        # asks user what their favourite drink is
        drink = input("What is your favourite drink? ")
        # then prints out the users favourite meal and drink
        print("Thank you " + user + " Your favourite three course meal consists of: ")
        print("A starter of " + starter + "," + " a main course of " + main_course + ", " + dessert + " for dessert")
        # then prints the users favourite drink
        print(" and don't forget your favourite drink of " + drink + "!")


# calling function
favourite_meal()
