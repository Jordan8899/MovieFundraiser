# IMPORTS GO HERE
import re
import pandas

# ==================================================
# FUNCTIONS GO HERE


def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        # checks if name is blank
        if response != "":
            return response
        # prints error message if name is blank
        else:
            print("Sorry - This cannot be blank!")
            print()


def int_check(question):

    error = "Sorry - Please enter a whole number more than 0"

    valid = False
    while not valid:

        # ask user for age and check if is valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        # if an integer is not entered, display an error message
        except ValueError:
            print(error)

    print()


def check_tickets(tickets_sold, ticket_limit):
    # tells user how seats are left
    if tickets_sold < ticket_limit - 1:
        print("You have {} seats "
              "left".format(ticket_limit - tickets_sold))

    else:
        print("*** There is only ONE seat left! ***")

    return ""


def get_ticket_price():
    age = int_check("Age:")
    print()

    if age < 12:
        print("Sorry - You are too young for this movie.")
        print()
        return "invalid ticket price"

    if age > 130:
        print("Sorry - Your input is too big, it looks like a mistake")
        print()
        return "invalid ticket price"

    if age < 16:
        price_of_ticket = 7.5

    elif age < 65:
        price_of_ticket = 10.5

    else:
        price_of_ticket = 6.5

    return price_of_ticket


def string_check(choice, options):

    is_valid = ""
    chosen = ""

    for var_list in options:

        if choice in var_list:

            chosen = var_list[0].title()
            is_valid = "yes"
            break

        else:
            is_valid == "no"

    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


def get_snack():

    number_regex = "^[1-9]"

    # valid snacks holds list of all snacks
    # each item in valid snacks is a list with,
    # valid options for each snack - full name, letter code,
    # and any possible abbreviations

    valid_snacks = [
        ["popcorn", "p", "pop", "corn", "a"],
        ["M&Ms", "MMs", "m&ms", "mms", "m", "b"],
        ["pita chips", "chips", "pc", "pita", "c"],
        ["orange juice", "orange j" "o juice", "oj", "d"],
        ["water", "w", "h20", "e"]
    ]

    print("Snack Options:")
    print("A. Popcorn")
    print("B. M&Ms")
    print("C. Pita Chips")
    print("D. Orange Juice")
    print("E. Water")
    print()
    print("- Enter number then snack, ex: 3 chips")
    print("- Max of 4 for each Snack!")
    print()
    print("- Type 'xxx' to exit")
    print()

    # holds snack order for single user
    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx" or desired_snack != "n":

        snack_row = []

        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            return snack_order

        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1
            desired_snack = desired_snack

        desired_snack = desired_snack.strip()

        snack_choice = string_check(desired_snack, valid_snacks)

        if amount >= 5:
            print("Sorry - Only 4 maximum of the same snack!")
            snack_choice = "invalid choice"
            amount = ""

        snack_row.append(amount)
        snack_row.append(snack_choice)

        if snack_choice != "xxx" and snack_choice != "invalid choice":

            print("Snack Choice: {} {}".format(amount, snack_choice))
            snack_order.append(snack_row)

        else:
            print("Sorry - What you entered is invalid!")

        print()
    print()


# ==================================================
# VARIABLES GO HERE
MAX_TICKETS = 5

name = ""

ticket_count = 0
ticket_sales = 0

# ==================================================
# DATAFRAME STUFF GOES HERE
# details
all_names = []
all_tickets = []

popcorn = []
mms = []
pita_chips = []
orange_juice = []
water = []

snack_lists = [popcorn, mms, pita_chips, orange_juice, water]

surcharge_mult_list = []

summary_headings = ["Popcorn", "M&Ms", "Pita Chips", "Orange Juice",
                    "Water", "Snack Profit", "Ticket Profit", "Surcharge Profit",
                    "Total Profit"]

summary_data = []

# movie data dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'M&Ms': mms,
    'Pita Chips': pita_chips,
    'Orange Juice': orange_juice,
    'Water': water,
    'Surcharge_Multiplier': surcharge_mult_list
}

# snack price dictionary
price_dict = {
    'Popcorn': 2.5,
    'M&Ms': 3,
    'Pita Chips': 4.5,
    'Orange Juice': 3.25,
    'Water': 2,
}

summary_data_dict = {
    'Item': summary_headings,
    'Amount': summary_data
}

# ==================================================
# LISTS GO HERE
# valid options for yes/no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# holds snack order for a single user
snack_order = []

# valid options for cash/card checker
payment_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

# ==================================================
# MAIN PROGRAM STARTS HERE
# execute program if exit code has not been received and there are tickets left
while name != "xxx" and ticket_count < MAX_TICKETS:

    # check that number of tickets has not been exceeded
    check_tickets(ticket_count, MAX_TICKETS)

# ==================================================
    # GET DETAILS
    # ASK USER FOR NAME
    # name cannot be blank
    name = not_blank("Name:")
    print()

    if name == "xxx":
        continue

# ==================================================
    # ASK USER FOR AGE
    # make sure age is within range
    # determine ticket price according to age
    ticket_price = get_ticket_price()

    if ticket_price == "invalid ticket price":
        continue

    ticket_count += 1
    ticket_sales += ticket_price

    # puts details in the dataframe
    name = name.title()
    all_names.append(name)
    all_tickets.append(ticket_price)

# ==================================================
    # ASK USER FOR SNACKS
    snack_order = get_snack()

    for item in snack_lists:
        item.append(0)

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

    print()
# ==================================================
    # ASK FOR PAYMENT METHOD + SURCHARGE
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method - cash/credit").strip().lower()
        how_pay = string_check(how_pay, payment_method)
    print()

    if how_pay == "Credit":
        surcharge_multiplier = 0.05
    else:
        surcharge_multiplier = 0

    surcharge_mult_list.append(surcharge_multiplier)

# ==================================================
# DATAFRAME PRINTS HERE - PART 1

movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

movie_frame["Snacks"] = \
    movie_frame['Popcorn'] * price_dict['Popcorn'] + \
    movie_frame['M&Ms'] * price_dict['M&Ms'] + \
    movie_frame['Pita Chips'] * price_dict['Pita Chips'] + \
    movie_frame['Orange Juice'] * price_dict['Orange Juice'] + \
    movie_frame['Water'] * price_dict['Water']

movie_frame["Sub Total"] = \
    movie_frame['Ticket'] + \
    movie_frame['Snacks']

movie_frame['Surcharge'] = \
    movie_frame['Sub Total'] * movie_frame['Surcharge_Multiplier']

movie_frame['Total'] = movie_frame['Sub Total'] + \
    movie_frame['Surcharge']

movie_frame = movie_frame.rename(columns={'Orange Juice': 'OJ',
                                          'Pita Chips': 'Chips',
                                          'Surcharge_Multiplier': "SM"})

# ==================================================
# PROFIT CALCULATIONS HERE
# calculate snack profit
for item in snack_lists:
    summary_data.append(sum(item))

snack_total = movie_frame['Snacks'].sum()
snack_profit = snack_total * 0.2
summary_data.append(snack_profit)

# calculate ticket profit
ticket_profit = ticket_sales - (5 * ticket_count)
summary_data.append(ticket_profit)

total_profit = snack_profit + ticket_profit
summary_data.append(total_profit)

# ==================================================
# DATAFRAME PRINTS HERE - PART 2
summary_frame = pandas.DataFrame(summary_data_dict)
summary_frame = summary_frame.set_index('Item')

pandas.set_option('display.max_columns', None)

pandas.set_option('precision', 2)

print()
print("*** Ticket / Snack Information ***")
print("Note: for full details please visit excel file called Movie Fundraiser")
print()
print(movie_frame[['Ticket', 'Snacks', 'Sub Total', 'Surcharge', 'Total']])

print("*** Profit / Snack Summary ***")
print()
print(summary_frame)

# ==================================================
# POST MAIN PROGRAM/PROFIT CALCULATOR/TICKET COUNT GOES HERE
print("Ticket Profit: ${:.2f}".format(ticket_profit))

if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. \n"
          "There are {} places still available"
          .format(ticket_count, MAX_TICKETS - ticket_count))