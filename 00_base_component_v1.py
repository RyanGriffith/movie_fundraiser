# import statements

# functions go here
# not blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error_message)
    # integer checker


low_number = 12
high_number = 130


def int_check(question):
    error = "Please enter a whole number between {} and {}".format(low_number, high_number)

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
                return age

        # if an integer is not entered, display error
        except ValueError:
            print(error)
    # ticket price


profit = 0

# *** main routine ***

# set up dictionaries / lists needed to hold data

# ask user if they have used the program before

# loop to get ticket details

name = " "
count = 0
MAX_TICKETS = 5

while name != "quit" and count < MAX_TICKETS:

    # tells user how many seats are left
    if count < 4:
        print("You have {} seats left".format(MAX_TICKETS - count))

    # warns user of one seat left
    else:
        print("*** THERE IS ONE SEAT LEFT ***")

    # get name not blank
    name = not_blank("Name: ", "Sorry - this can't be blank")
    count += 1
    print()
    if name == "quit":
        count -= 1
        break

    # get age between 12 - 130
    age = int(input("Age: "))

    # ticket price
    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    profit_made = ticket_price - 5
    profit += profit_made

    print("{} : ${:.2f}".format(name, ticket_price))

if count == MAX_TICKETS:
    print("You have sold all available tickets!")

else:
    print("You have sold {} tickets. There are still {} places available".format(count, MAX_TICKETS - count))

    # loop to ask for snacks

    # calculate snack price

    # ask for payment method

    # integer checker

# output data to text file
