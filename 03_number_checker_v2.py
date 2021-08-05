# function goes here

lownumber = 12
highnumber = 130

def int_check(question):

    error = "Please enter a whole number between {} and {}".format(lownumber, highnumber)

    valid = False
    while not valid:

        # ask user for number and if valid
        try:
            response = int(input(question))

            if response <= 11:
                print(error)

            elif response >= 131:
                print(error)

            else:
                return response

        # if an integer is not entered, display error
        except ValueError:
            print(error)

# main routine goes here

age = int_check("age: ")
