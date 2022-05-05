# Definitions
pay1 = ["credit", "card"]
pay2 = ["cash", "money"]
ticket_price = 0
users_snacks_name = []
users_snacks_amount = []
cost = 0
snack = ""
amount = 0
count = 0
max_tickets = 150
names = []
ages = []
ticket_child = 0
ticket_adult = 0
ticket_senior = 0
exit = False

# Functions

# String checker including M&M used for name, snack, pay
def string_input(question):
    while True:
        try:
            response = str(input(question)).strip()

            if response.isalpha():
                return response

            elif response == "m&m" or response == "M&M":
                return response

            else:
                print("Please input a valid response, this response can only contain letters")
        except ValueError:
            print("Error\n")


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

# Main Routine

# Privacy info
print("This program will lead you through buying tickets and snacks. \n"
      "We will only store your private information for this fundraiser  \n"
      "We will not share your private information.\n"
      "Please enter all following questions and thank you for helping us raise money \n")

while not exit and count <= max_tickets:
    # Ticket Details
    print("For ages 12 - 15 tickets will cost $7.50\n"
          "For ages 16 - 64 tickets will cost $10.50\n"
          "For ages 64+ tickets will cost $6.50\n")

    # Name variable calling the function
    name = string_input("What's your name? ")
    names.append(name)

    # Count
    count += 1

    # Age variable using number_input function
    age = number_input("What's your age? ")
    ages.append(age)

    # Ticket Price
    if age in range(12, 15):
        ticket_price += 7.5
        ticket_child += 1

    elif age in range(16, 64):
        ticket_price += 10.5
        ticket_adult += 1

    elif age in range(65, 130):
        ticket_price += 6.5
        ticket_senior += 1

    print("Ticket Price is ${:.2f}".format(ticket_price))

    # Snack while loop only exits when user inputs exit + snack details / information
    print("The snacks we have for offer are: \n"
          "\nPopcorn \n"
          "M&M \n"
          "Pita Chips \n"
          "Orange Juice \n"
          "Water \n"
          "\nTo buy snacks please enter the snacks name \n"
          "Then enter the quantity of snacks you want\n")

    while True:
        snack = string_input("What snack do you want? ")

        # Exit code statement
        if snack != "exit":
            amount = int_input("How much {} do you want? ".format(snack))

        # Sets users input to remove spaces and lower cases
        snack_check = snack.lower().replace(" ", "")

        if snack_check == "popcorn":
            cost += 2.5 * amount
            users_snacks_name.append("Popcorn")
            users_snacks_amount.append(amount)

        elif snack_check == "m&m" or snack_check == "mandm":
            cost += 3 * amount
            users_snacks_name.append("M&M")
            users_snacks_amount.append(amount)

        elif snack_check == "pitachips":
            cost += 4.5 * amount
            users_snacks_name.append("Pita Chips")
            users_snacks_amount.append(amount)

        elif snack_check == "oj" or snack_check == "orangejuice":
            cost += 3.25 * amount
            users_snacks_name.append("Orange Juice")
            users_snacks_amount.append(amount)

        elif snack_check == "water":
            cost += 2 * amount
            users_snacks_name.append("Water")
            users_snacks_amount.append(amount)

        elif snack_check == "exit":
            break

        else:
            print("Please input valid snack or type 'exit' to continue")

        snack_yes_no = string_input("Would you like to buy another snack? ")
        if snack_yes_no == "no" or snack_yes_no == "nah":
            break

    exit_chance = string_input("Would you like to buy another ticket? ").replace(" ", "").lower()
    if exit_chance == "no":
        exit = True

# Finds amount of snacks user has inputted
len_user_snack_name = len(users_snacks_name)

# For loop that prints how many snacks user has inputted
for i in range(len_user_snack_name):
    print("You will get {} {}".format(users_snacks_amount[i], users_snacks_name[i]))

# Payment method, card or credit + total cost calculation
total_cost = ticket_price + cost

while True:
    payment_method = string_input("How would you like to pay (Cash or Card)? ")
    if payment_method in pay1:
        surcharge = total_cost * 1.05
        total_cost = surcharge
    elif payment_method in pay2:
        break
    else:
        print("Please input 'cash' or 'card'")

# Total Cost
print("Your total cost is: ${:.2f}".format(total_cost))

# Profit
snack_profit = 0.2 * cost
profit = ticket_price + snack_profit
