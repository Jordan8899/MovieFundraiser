pay1 = "credit"
pay2 = "cash"
ticket_price = 0
snack_list = ["Popcorn", "M&M", "Pita Chips", "Orange Juice", "Water", "OJ"]
users_snacks_name = []
users_snacks_amount = []
cost = 0
snack = ""
amount = 0


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


def int_input(question):
    while True:
        try:
            response = int(input(question))

            if response > 0:
                return response

        # Error message if user inputs incorrect characters
        except ValueError:
            print("Error, please only input numbers\n")


# Number checker function that can be called infinite times
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


# Age variable using number_input function
age = number_input("What's your age? ")

# Ticket Price
if age in range(12, 15):
    ticket_price += 7.5

elif age in range(16, 64):
    ticket_price += 10.5

elif age in range(65, 130):
    ticket_price += 6.5

print("Ticket Price is ${:.2f}".format(ticket_price))

# Snack while loop only exits when user inputs exit
while snack != "exit":
    snack = string_input("What snack do you want? ")

    # Exit code statement
    if snack != "exit":
        amount = int_input("How much {} do you want? ".format(snack))

    # Sets users input
    snack_check = snack.lower().replace(" ", "")

    if snack_check == "popcorn":
        cost += 2.5 * amount
        users_snacks_name.append("Popcorn")

    elif snack_check == "m&m":
        cost += 3 * amount
        users_snacks_name.append("M&M")

    elif snack_check == "pitachips":
        cost += 4.5 * amount
        users_snacks_name.append("Pita Chips")

    elif snack_check == "oj" or snack_check == "orangejuice":
        cost += 3.25 * amount
        users_snacks_name.append("Orange Juice")

    elif snack_check == "water":
        cost += 2 * amount
        users_snacks_name.append("Water")

    else:
        print("Please input valid snack or type 'exit' to continue")

    users_snacks_amount.append(amount)

# Finds amount of snacks user has inputted
len_user_snack_name = len(users_snacks_name)

# For loop that prints how many snacks user has inputted
for i in range(len_user_snack_name):
    print("You will get {} {}".format(users_snacks_amount[i], users_snacks_name[i]))

# Payment method, card or credit + total cost calculation
total_cost = ticket_price + cost

payment_method = string_input("How would you like to pay? ")

if payment_method == pay1:
    surcharge = total_cost * 1.05
    total_cost = surcharge

# Total Cost
print("Your total cost is: ${:.2f}".format(total_cost))

# Profit
profit = ticket_price + cost
