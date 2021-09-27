import re

# functions
def string_check(choice, options):

    is_valid = ""
    chosen = ""

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
        return "Invalid choice"


# regular expression
number_regex = "^[1-9]"

# valid snacks list
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&Ms", "m&ms", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
    ["orange juice", "oj", "juice", "e"]
]

# valid choice
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]
snack_order = []

# ask user if want snacks
check_snack = "Invalid choice"
while check_snack == "Invalid choice":
    want_snack = input("do you want snacks?: ").lower()
    check_snack = string_check(want_snack, yes_no)

# if want snack is yes
if check_snack == "yes" or "y":

    desired_snack = ""
    while desired_snack != "quit":
        # ask user what snack
        desired_snack = input("snack: ").lower

        if desired_snack == "quit":
            break

        # if item has a number
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1
            desired_snack = desired_snack

        # remove white space
        desired_snack = desired_snack.strip()

        # check if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks)

        # check snack amount
        if amount >= 5:
            print("sorry - we have a 4 snack maximum")
            snack_choice = "Invalid choice"

        # add snack and amount
        amount_snack = "{}  {}".format(amount, snack_choice)

        # check that snack is not the exit code
        if snack_choice != "quit" and snack_choice != "Invalid choice":
            snack_order.append(amount_snack)

# show snack orders
print()
if len(snack_order) == 0:
    print("snacks ordered: none")

else:
    print("snacks ordered: ")

    for item in snack_order:
        print(item)
