def yes_no(question):

    error = "please answer 'Yes / No'"

    valid = False
    while not valid:

        # ask question and put in lower case
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print(error)

# main routine

for item in range (0 , 6):

    want_snacks = yes_no("do you want snacks?")
    print("Answer OK, You said:", want_snacks)
    print()
