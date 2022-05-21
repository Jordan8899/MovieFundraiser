import re

def get_snack():
    number_regex = "^[1-9]"

    valid_snacks = [
        ["popcorn", "p", "pop", "corn"],
        ["M&Ms", "m&m's", "mms", "mm", "m"],
        ["pita chips", "chips", "pc", "pita"],
        ["water", "w"],
        ["orange juice", "oj", "o", "juice", "orange"]
    ]

    snack_list = []

    wanted_snack = ""
    while wanted_snack != "exit":

        snack_row = []
        wanted_snack = input("Snack: ").lower()
        print()

        if wanted_snack == "exit":
            return wanted_snack

        if re.match(number_regex, wanted_snack):
            amount = int(wanted_snack[0])
            wanted_snack = wanted_snack[1:]
        else:
            amount = 1
            wanted_snack = wanted_snack

        wanted_snack.replace(" ", "")

        if wanted_snack == "invalid":
            print("Please input a valid snack")
            print()

        if amount >= 5:
            print("Sorry we have a snack amount limit of 4 per person")
            snack_choice = "invalid"

        snack_row.append(amount)
        snack_row.append(snack_choice)

        if snack_choice != "exit" and snack_choice != "invalid":
            snack_list.append(snack_row)
