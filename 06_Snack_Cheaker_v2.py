# Function goes here
def string_check(choice, options):

    for var_list in options:

        # if the snack is in one of the lists
        if choice in var_list:

            # get full name of snack
            # in title case so it looks nice
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen option not valid
        else:
            is_valid = "no"

    # if snack is no OK ask again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


# valid snacks list
# with valid letter code
# abbreviations
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]

# loop start (6 for testing)
for item in range(0, 6):

    # ask user for desired snack
    desired_snack = input("Snack: ").lower()

    # check if snack is valid
    snack_choice = string_check(desired_snack, valid_snacks)
    print("Snack Choice: ", snack_choice)
