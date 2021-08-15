def string_checker(question, to_check):

    error = "please answer 'Yes / No'"

    valid = False
    while not valid:

        # ask question and put in lower case
        response = input(question).lower()

        if response in to_check:
            return response

        else:
            for item in to_check:

                # checks if response is the first letter of list items
                if response == item[0]:

                    # returns entire response rather than just letter
                    return item
        print("sorry that isn't a valid item")


# main routine

for item in range (0 , 6):

    want_snacks = string_checker("do you want snacks?", ["yes", "no"])
    print("Answer OK, You said:", want_snacks)
    print()
