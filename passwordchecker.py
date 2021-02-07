import re


def validate():
    # helps user to create a strong password
    print("Please use this programme to create a strong password for your account")
    # starts loop
    while True:
        password = input("Enter a password: ")
        # checks that the password is the right length
        if len(password) < 8:
            print("Make sure your password is at least 8 letters")
        elif re.search('[0-9]', password) is None:
            # tells user to add a number
            print("Please add a number to your password")
        elif re.search('[A-Z]', password) is None:
            # tells user to add a capital letter
            print("Please add a capital letter to your password")
        elif re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', password) is None:
            # tells user to add special character
            print("Your password is medium, please enter a special character to your password")
            # tells user that their password is now strong
        else:
            print("Yay! Your password is Strong, please choose this as your password")
        # lets user exit program or try again
        rerun = input("Try again? 1 for Yes 2 for No ")
        if rerun != "1":
            break


# runs function
validate()
