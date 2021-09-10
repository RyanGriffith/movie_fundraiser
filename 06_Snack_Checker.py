# valid snacks hold list of all valid snacks
valid_snacks = [
    ['Popcorn', 'popcorn', 'p', 'corn', 'a'],
    ['M&Ms', 'mms', 'MMS', 'm', 'b'],
    ['Pita Chips', 'pita chips', 'pc', 'chips', 'c'],
    ['Water', 'w', 'd', 'water', 'liquid']
]

# initialise variables
snack_ok = ""
snack = ""

# loop 3 times for fast testing
for item in range(0, 1):

    # asks user for desired snack
    desired_snack = input("Snack: ")

    for var_list in valid_snacks:

        # if the snack is in the list
        if desired_snack in var_list[0]:

            # get full name of snack
            # in title case
            snack = var_list[0].title()
            snack_ok = "yes"
            break
        # if the chosen snack isn't valid
        else:
            snack_ok = "no"
            break
    # if snack not ok - ask again
    if snack_ok == "yes":
        print("snack choice: ", snack)
    else:
        print("invalid snack")
