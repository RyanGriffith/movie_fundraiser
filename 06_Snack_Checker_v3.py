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

yes_no = [
    ["yes", "y"],
    ["no", "n"]
]
no_message = ""

# holds snack choice
snack_order = []


# ask if want snacks
check_snack = "invalid choice"
while check_snack == "invalid choice" or yes_no == "yes":
    want_snack = input("do you want to order snacks?: ").lower()
    check_snack = string_check(want_snack, yes_no)

# loop start (6 for testing)
for item in range(0, 6):

    # ask user for desired snack
    desired_snack = input("Snack: ").lower()

    # check if snack is valid
    snack_choice = string_check(desired_snack, valid_snacks)
    print("Snack Choice: ", snack_choice)

# if they say yes to snacks
if check_snack == "yes":

    desired_snack = ""
    while desired_snack != "xxx":
        # asks for desired snack
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            break
        snack_choice = string_check(desired_snack, valid_snacks)
        print("Snack Choice: ", snack_choice)

        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_choice)

# show snack order
print()
if len(snack_order) == 0:
    print("Snacks Ordered: None")

else:
    print("Snacks Ordered: ")

    for item in snack_order:
        print(item)

