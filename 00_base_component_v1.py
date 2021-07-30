# import statements

# functions go here
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry - this can't be blank")
# *** main routine ***

# set up dictionaries / lists needed to hold data

# ask user if they have used the program before

# loop to get ticket details

    # get name (can't be blank)
name = not_blank("Name: ")
name = " "
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
    print("You have {} seats left ".format(MAX_TICKETS - count))

    # get details
    name = input("name: ")
    count += 1
    print()
    if name == "xxx":
        count -= 1
    if name == " ":
        print(error_message)

if count == MAX_TICKETS:
    print("You have sold all available tickets!")
else:
    print("You have sold {} tickets. There are still {} places available".format(count, MAX_TICKETS - count))
    # get age (between 11 and 130)

    # loop to ask for snacks

    # calculate snacks price

    # ask for payment method

# calculate total sales and profit

# output data to text file
