# valid snacks hold list of all valid snacks
valid_snacks = [
    ['Popcorn', 'p', 'corn', 'a'],
    ['M&Ms', 'mms', 'MMS', 'm', 'b'],
    ['Pita Chips', 'pc', 'chips', 'c'],
    ['Water', 'w', 'd']
]

# initialise variables
snack_ok = ""
snack = ""

# loop 3 times for fast testing
for item in range(0, 3):

    # asks user for desired snack
    desired_snack = input("Snack: ").lower()

    for var_list in valid_snacks:

        # if the snack is in the list
        if desired_snack in var_list:

            # get full name of snack
            # in title case
            snack = var_list[0].title()
            snack_ok = "yes"
            break
        # if the chosen snack isn't valid
        else:
            snack_ok = "no"
    # if snack not ok - ask again
    if snack_ok == "yes:":
        print("snack choice: ", snack)
    else:
        print("invalid snack")
