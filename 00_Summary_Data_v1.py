# Imports
import pandas
import re

#  Snack Lists
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []
snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# User information Lists
names = []
ages = []

# Ticket and surcharge lists
total_tickets = []
surcharge_multi_list = []

# Set Definitions
pay1 = ["credit", "card"]
pay2 = ["cash", "money"]
cost = 0
ticket_price = 0
ticket_count = 0
MAX_TICKETS = 150
exit = False
no_words = ["no", "nah", "negative", "incorrect", "exit"]
yes_words = ["yes", "yea", "ya", "positive", "sure", "correct"]
ticket_sales = 0
surcharge = 0

# Summary Data
summary_headings = ["Popcorn", "M&M's", "Pita Chips", "Water", "Orange Juice", "Snack Profit", "Ticket Profit", "Total Profit"]

summary_data = []

# Summary Dictionary
movie_data_dictornary = {
    "Name": names,
    'Ticket': total_tickets,
    "Popcorn": popcorn,
    "Water": water,
    "Pita Chips": pita_chips,
    "M&Ms'": mms,
    "Orange Juice": orange_juice,
    "Surcharge": surcharge_multi_list
}

summary_data_dictornary = {
    "Item": summary_headings,
    "Amount": summary_data
}

# Price Dictionary
price_dict = {
    "Popcorn": 2.5,
    "Water": 2,
    "Pita Chips": 4.5,
    "M&Ms'": 3,
    "Orange Juice": 3.25
}

# Functions

# String checker
def string_input(question):
    while True:
        try:
            response = str(input(question)).strip()

            if response.isalpha():
                return response

            else:
                print("Please input a valid response, this response can only contain letters")
        except ValueError:
            print("Error\n")

def snack_input_checker(choice, options):
    for var_list in options:
        # If the snack is in the list it will return snack name
        if choice in var_list:
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # If chosen option isn't a valid response make it invalid
        else:
            is_valid = "no"

    # Snack Loop if incorrect response
    if is_valid == "yes":
        return chosen
    else:
        return "invalid"


# Number Checker function for things other than age
def int_input(question):
    while True:
        try:
            response = int(input(question))

            if response > 0:
                return response

        # Error message if user inputs incorrect characters
        except ValueError:
            print("Error, please only input numbers\n")


# Number checker function for age
def number_input(question):
    while True:
        try:
            response = int(input(question))

            # If statement checking viable age
            if response < 12 or response >= 130:

                if response < 12:
                    print("You're too young to be doing this by yourself")

                elif response >= 130:
                    print("Please enter your real age")

            elif 11 < response <= 130:
                return response

        # Error message if user inputs incorrect characters
        except ValueError:
            print("Please only input numbers\n")

def check_tickets(tickets_sold, tickets_limit):
    # This tells user how many seats are left
    if tickets_limit - tickets_sold == 1:
        print("There is only 1 seat left available")
    else:
        print("There are {} seats left".format(tickets_limit - tickets_sold))

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
            amounts = int(wanted_snack[0])
            wanted_snack = wanted_snack[1:]
        else:
            amounts = 1
            wanted_snack = wanted_snack

        wanted_snack.strip()

        snack_choice = snack_input_checker(wanted_snack, valid_snacks)

        if snack_choice == "invalid":
            print("Please input a valid snack")

        if amounts >= 5:
            print("Sorry we have a snack amounts limit of 4 per person")
            snack_choice = "invalid"

        snack_row.append(amounts)
        snack_row.append(snack_choice)

        if snack_choice != "exit" and snack_choice != "invalid":
            snack_list.append(snack_row)

# **************************************************************
#                           Main Routine
# **************************************************************

# Privacy info
print("This program will lead you through buying tickets and snacks. \n"
      "We will only store your private information for this fundraiser  \n"
      "We will not share your private information.\n"
      "Please enter all following questions and thank you for helping us raise money \n")

while not exit and ticket_count <= MAX_TICKETS - 1:

    # How many seats are left
    check_tickets(ticket_count, MAX_TICKETS)

    # Ticket Details
    print("For ages 12 - 15 tickets will cost $7.50\n"
          "For ages 16 - 64 tickets will cost $10.50\n"
          "For ages 64+ tickets will cost $6.50\n")

    # Name variable calling the function
    name = string_input("What's your name? ")
    names.append(name)

    # Age variable using number_input function
    age = number_input("What's your age? ")
    ages.append(age)

    # Ticket Price
    if age in range(12, 15):
        ticket_price = 7.5

    elif age in range(16, 64):
        ticket_price = 10.5

    elif age in range(65, 130):
        ticket_price = 6.5

    total_tickets.append(ticket_price)
    ticket_count += 1
    ticket_sales += ticket_price

    print("\nTicket Price is ${:.2f}\n".format(ticket_price))
    # Snack while loop only exits when user inputs exit + snack details / information
    print("The snacks we have for offer are: \n"
          "\nPopcorn \n"
          "M&M \n"
          "Pita Chips \n"
          "Orange Juice \n"
          "Water \n"
          "\nTo buy snacks please enter the snacks name and to order more than one\n"
          "enter a number within 2 - 4 as we have a snack limit of 4 of any one item per person"
          "\nenter 'exit' to stop buying snacks\n")

    # Allows snacks to be brought
    snack_order = get_snack()

    # Adds snack amount to list
    for item in snack_lists:
        item.append(0)

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dictornary[to_find]
            add_list[-1] = amount

    # Payment method, card or credit
    while True:
        payment_method = string_input("How would you like to pay (Cash or Card)? ")

        if payment_method in pay1:
            surcharge = 0.05
            break
        elif payment_method in pay2:
            surcharge = 0
            break
        else:
            print("Please input 'cash' or 'card'")

        surcharge_multi_list.append(surcharge)

    # Allows user to buy more tickets if requested
    if MAX_TICKETS > 0:
        exit_chance = string_input("Would you like to buy another ticket? ").replace(" ", "").lower()
        if exit_chance in no_words:
            exit = True
    else:
        exit = True

# Pandas Frame
movie_frame = pandas.DataFrame(movie_data_dictornary)
movie_frame = movie_frame.set_index("Name")

movie_frame["Snacks"] = \
    movie_frame["Popcorn"]*price_dict["Popcorn"] + \
    movie_frame["Water"]*price_dict["Water"] + \
    movie_frame["Pita Chips"]*price_dict["Pita Chips"] + \
    movie_frame["M&Ms'"]*price_dict["M&Ms'"] + \
    movie_frame["Orange Juice"]*price_dict["Orange Juice"]

movie_frame["Sub Total"] = \
    movie_frame["Ticket"] + \
    movie_frame["Snacks"]

movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge_Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + \
    movie_frame["Surcharge"]

# Rename columns
movie_frame = movie_frame.rename(columns={"Orange Juice": "OJ",
                                          "Pita Chips": "Chips",
                                          "Surcharge_Multiplier": "SM"})

# Summary Dataframes
for item in snack_lists:
    summary_data.append(sum(item))

# Snack Profit
snack_total = movie_frame["Snacks"].sum()
snack_profit = snack_total * 0.2

# Ticket Profit
ticket_profit = ticket_sales - (5 * ticket_sales)

# Total Profit
total_profit = snack_profit + ticket_profit

# Format amount and add to lists
dollar_amounts = [snack_profit, ticket_profit, total_profit]
for item in dollar_amounts:
    item = "${:.2f}".format(item)
    summary_data.append(item)

# Summary Frame
summary_frame = pandas.DataFrame(summary_data_dictornary)
summary_frame = summary_frame.set_index("Item")

# Pandas Display
pandas.set_option("display.max_columns", None)

# CSV Files
movie_frame.to_csv("ticket_details.csv")
summary_frame.to_csv("snack_summary.csv")

print("\n**** Ticket and Snack Information ****\n")
print(movie_frame[["Ticket", "Sub Total", "Surcharge", "Total"]])
