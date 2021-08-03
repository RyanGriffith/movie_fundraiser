# import statements

# functions go here

#not blank error

def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error_message)

# number checker

def int_check(question, low_num, high_num):

    error = "Please enter a whole number between {} and {}".format(low_num, high_num)

    valid = False
    while not valid:

        # ask user for number and if valid
        try:
            response = int(input(question))

            if low_num <= response <= high_num:
                print(error)

            else:
                print(error)

        # if an integer is not entered, display error
        except ValueError:
            print(error)

# *** main routine ***

# set up dictionaries / lists needed to hold data

# ask user if they have used the program before

# loop to get ticket details

    # get name (can't be blank)

print("Order Name   ")

name = not_blank("Name: ", "Sorry - this can't be blank")

# initialise loop so that it runs at least once


count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    # tells user how many seats are left
    if count < 4:
        print("You have {} seats left".format(MAX_TICKETS - count))

    # warns user of one seat left
    else:
        print("*** THERE IS ONE SEAT LEFT ***")

    # get details
    name = input("name: ")
    count += 1
    print()
    if name == "xxx":
        count -= 1

if count == MAX_TICKETS:
    print("You have sold all available tickets!")

else:
    print("You have sold {} tickets. There are still {} places available".format(count, MAX_TICKETS - count))

# get age (between 11 and 130)

age = int_check("age: ", 12, 130)

# loop to ask for snacks

# calculate snacks price

# ask for payment method

# calculate total sales and profit

# output data to text file
